# options.json

In dit project werken meerdere tools samen: het aquarium in Unity, een vissenmaker in web en Python-scripts die het controleren. Via het bestandje `options.json` zorgen we dat al deze tools weten hoe een vis is opgebouwd. Alle onderdelen van het aquarium lezen deze lijst:

- de **validator** (`tools/validate_fish.py`) keurt een vis af als een keuze er niet in staat;
- de **Vissenmaker** (`maker/`) moet dezelfde keuzes tonen (`tools/check_maker.py` controleert dat);
- het **Unity-aquarium** krijgt de lijst via de website.

## Wat staat erin?

| Onderdeel | Betekenis |
| --- | --- |
| `body`, `fins`, `pattern`, `behavior` | Keuzes voor lichaam, vinnen, patroon en gedrag. Elke keuze heeft een `id` en een `label`. |
| `size`, `speed` | De toegestane groottes en snelheden, als vaste opties. |
| `limits` | De maximale lengte van `name` en `maker`. |
| `version` | Het versienummer van de options. |

- Het **`id`** is Engels en wordt gebruikt in code en visbestanden, bijvoorbeeld `"pointy"`. Verander een bestaand id nooit, want dan kloppen bestaande vissen niet meer.
- Het **`label`** is de Nederlandse tekst die mensen zien, bijvoorbeeld `"Puntig"`.

## Een nieuwe keuze toevoegen

Per onderdeel staan er bewust maar twee keuzes in. Voeg je er een toe, bijvoorbeeld een patroon `dots`, dan moet dat op drie plekken:

1. Hier in `options.json`: `{ "id": "dots", "label": "Stippen" }`
2. In de Vissenmaker: een keuzerondje en de CSS voor het voorbeeld.
3. In Unity: een onderdeel in de catalogus.

Controleer daarna met `python tools/validate_fish.py` en `python tools/check_maker.py`. Deze controles geven een foutmelding als er verschil zit tussen de drie onderdelen.
