"""Controleert de visbestanden in de map fish/.

Gebruik:
    python tools/validate_fish.py                 # controleer alle vissen
    python tools/validate_fish.py fish/bubbel.json  # controleer alleen deze vis

Exitcode 0 als alles klopt, 1 als er fouten zijn.
"""

import json
import re
import sys
from pathlib import Path

# Repository root
ROOT = Path(__file__).resolve().parent.parent

# Map met de vissen en de options-file
FISH_DIR = ROOT / "fish"
OPTIONS_FILE = ROOT / "shared" / "options.json"

# Deze velden worden gecontroleerd
REQUIRED_FIELDS = ["name", "maker", "body", "fins", "pattern", "colors", "size", "speed", "behavior"]
COLOR_PARTS = ["body", "fins", "pattern"]

# Velden die een id uit options.json moeten bevatten.
CHOICE_FIELDS = ["body", "fins", "pattern", "behavior"]
# Velden die een getal uit options.json moeten bevatten.
NUMBER_FIELDS = ["size", "speed"]

# Hier worden de namen van bestanden gecontroleerd met 'regular expressions'
# Een file mag alleen letters en cijfers bevatten en tussen de 1 tot 30 tekens hebben.
# Een color pattern is een hexadecimaal, bijvoorbeeld #ff26ab
FILE_ID_PATTERN = re.compile(r"^[a-z0-9-]{1,30}$")
COLOR_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}$")


def load_options(path=OPTIONS_FILE):
    """Leest options.json in en geeft het als dictionary terug"""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def fish_id_from_path(path):
    """De id van een vis is de bestandsnaam zonder .json."""
    return Path(path).stem


def show_path(path):
    """Toon een pad kort, bijvoorbeeld fish/henk.json."""
    path = Path(path).resolve()
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def validate_file_name(filename):
    """Controleert of de bestandsnaam een geldig id is."""
    errors = []
    path = Path(filename)
    if path.suffix != ".json":
        errors.append(f"{filename}: de bestandsnaam moet eindigen op .json")
    if not FILE_ID_PATTERN.match(path.stem):
        errors.append(
            f"{filename}: de bestandsnaam '{path.stem}' mag alleen kleine letters a-z, "
            "cijfers en '-' bevatten, en maximaal 30 tekens lang zijn"
        )
    return errors


def validate_text(data, field, max_length, filename):
    """Controleer een tekstveld zoals name of maker."""
    value = data[field]
    if not isinstance(value, str) or value.strip() == "":
        return [f"{filename}: '{field}' mag niet leeg zijn"]
    if len(value) > max_length:
        return [f"{filename}: '{field}' is {len(value)} tekens, maar mag maximaal {max_length} tekens zijn"]
    return []


def validate_colors(colors, filename):
    """Controleert het colors-object: drie kleuren in de vorm #rrggbb."""
    if not isinstance(colors, dict):
        return [f"{filename}: 'colors' moet een object zijn met de kleuren {', '.join(COLOR_PARTS)}"]

    errors = []
    for part in COLOR_PARTS:
        if part not in colors:
            errors.append(f"{filename}: 'colors.{part}' ontbreekt")
        elif not isinstance(colors[part], str) or not COLOR_PATTERN.match(colors[part]):
            errors.append(f"{filename}: 'colors.{part}' is '{colors[part]}', maar moet een kleur zijn zoals #ff8800")
    for part in colors:
        if part not in COLOR_PARTS:
            errors.append(f"{filename}: 'colors.{part}' is onbekend, toegestaan zijn: {', '.join(COLOR_PARTS)}")
    return errors


def validate_fish(data, options, filename):
    """Controleert één vis en geeft een lijst met foutmeldingen terug.

    Een lege lijst betekent dat er geen fouten zijn.
    """
    if not isinstance(data, dict):
        return [f"{filename}: het bestand moet een JSON-object zijn, dus beginnen met {{"]

    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"{filename}: het veld '{field}' ontbreekt")
    for field in data:
        if field not in REQUIRED_FIELDS:
            errors.append(f"{filename}: het veld '{field}' is onbekend, haal het weg of controleer de spelling")

    limits = options["limits"]
    if "name" in data:
        errors += validate_text(data, "name", limits["nameMaxLength"], filename)
    if "maker" in data:
        errors += validate_text(data, "maker", limits["makerMaxLength"], filename)

    for field in CHOICE_FIELDS:
        if field not in data:
            continue
        allowed = [option["id"] for option in options[field]]
        if data[field] not in allowed:
            errors.append(f"{filename}: '{field}' is '{data[field]}', maar moet een van deze zijn: {', '.join(allowed)}")

    for field in NUMBER_FIELDS:
        if field not in data:
            continue
        allowed = options[field]
        value = data[field]
        # True en False tellen in Python als 1 en 0, die willen we niet.
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value not in allowed:
            allowed_text = ", ".join(str(number) for number in allowed)
            errors.append(f"{filename}: '{field}' is '{value}', maar moet een van deze zijn: {allowed_text}")

    if "colors" in data:
        errors += validate_colors(data["colors"], filename)

    return errors


def check_unique_names(fish_by_file):
    """Controleert dat geen twee vissen dezelfde naam hebben (hoofdletters tellen niet mee).

    fish_by_file is een dictionary: bestandsnaam -> visdata.
    Geeft een dictionary terug: bestandsnaam -> foutmelding, voor elke dubbele vis.
    """
    errors = {}
    seen = {}
    for filename, data in fish_by_file.items():
        name = data.get("name") if isinstance(data, dict) else None
        if not isinstance(name, str) or name.strip() == "":
            continue
        key = name.strip().lower()
        if key in seen:
            errors[filename] = f"{filename}: de naam '{name}' wordt al gebruikt in {seen[key]}, kies een andere naam"
        else:
            seen[key] = filename
    return errors


def load_fish_file(path):
    """Leest een visbestand. Geeft (data, fouten) terug."""
    filename = show_path(path)
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file), []
    except json.JSONDecodeError as error:
        return None, [f"{filename}: geen geldige JSON (regel {error.lineno}, kolom {error.colno}): {error.msg}"]
    except UnicodeDecodeError:
        return None, [f"{filename}: het bestand moet opgeslagen zijn als UTF-8"]
    except OSError as error:
        return None, [f"{filename}: kan het bestand niet lezen ({error.strerror})"]


def validate_files(paths, options):
    """Controleert een lijst visbestanden.

    Geeft (geldige_vissen, fouten) terug. geldige_vissen is een dictionary
    id -> visdata met alleen de vissen zonder fouten.
    """
    errors = []
    loaded = {}
    for path in sorted(paths):
        filename = show_path(path)
        file_errors = validate_file_name(filename)
        data, load_errors = load_fish_file(path)
        file_errors += load_errors
        if data is not None:
            file_errors += validate_fish(data, options, filename)
            loaded[filename] = data
        errors += file_errors
        if file_errors:
            loaded.pop(filename, None)

    # Een dubbele naam keurt de tweede vis af (op alfabetische volgorde).
    duplicates = check_unique_names(loaded)
    for filename, message in duplicates.items():
        errors.append(message)
        loaded.pop(filename)

    valid_fish = {fish_id_from_path(filename): data for filename, data in loaded.items()}
    return valid_fish, errors


def main(arguments):
    try:
        options = load_options()
    except (OSError, json.JSONDecodeError) as error:
        print(f"Kan {show_path(OPTIONS_FILE)} niet lezen: {error}")
        return 1

    if arguments:
        paths = [Path(argument) for argument in arguments]
    else:
        paths = list(FISH_DIR.glob("*.json"))

    if not paths:
        print("Geen visbestanden gevonden in fish/.")
        return 0

    valid_fish, errors = validate_files(paths, options)

    for message in errors:
        print(message)

    if errors:
        print(f"\n{len(errors)} fout(en) gevonden. {len(valid_fish)} van de {len(paths)} vissen zijn goed.")
        return 1

    print(f"Alles klopt! {len(valid_fish)} vis(sen) gecontroleerd.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
