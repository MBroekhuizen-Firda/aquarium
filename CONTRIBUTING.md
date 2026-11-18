# Bijdragen aan het Aquarium

In dit project leer je hoe je bijdraagt aan een open-sourceproject met een **fork** en een **pull request** (PR).

## Je eerste bijdrage: voeg je vis toe

Er zijn twee routes. Met de **snelle route** stuur je je vis in vanuit de Vissenmaker, zonder iets te installeren. Met de **route met clone en branch** werk je zoals een ontwikkelaar: met Git op je eigen computer. Wil je leren samenwerken met Git, kies dan de tweede route.

## Snelle route: Stuur in via GitHub

Je hebt alleen een GitHub-account nodig. Log eerst in op [github.com](https://github.com).

1. Ontwerp je vis in de [Vissenmaker](https://firda-software-development-drachten.github.io/aquarium/maker/).
2. Klik op **Stuur in via GitHub**. GitHub opent een nieuw bestand in de map `fish/`, met je vis er al in.
3. Klik op **Commit changes...** en daarna op **Propose changes**. GitHub maakt nu zelf een fork en een branch voor je.
4. Klik op **Create pull request**. Vul het formulier in en klik nog een keer op **Create pull request**.

Daarna gaat het verder zoals bij stap 8 hieronder: er draait een automatische controle en een docent bekijkt je PR.

> **Privacy:** dit is een openbare repository en dus voor iedereen zichtbaar. Gebruik bij `maker` alleen je voornaam of een bijnaam.

## Route met clone en branch

### 1. Fork de repository

Ga naar [github.com/Firda-Software-Development-Drachten/aquarium](https://github.com/Firda-Software-Development-Drachten/aquarium) en klik rechtsboven op **Fork**. Je krijgt nu je eigen kopie van het project onder je eigen account.

### 2. Clone je fork

Clone **je eigen fork**, niet het origineel:

```bash
git clone https://github.com/<jouw-gebruikersnaam>/aquarium.git
cd aquarium
```

### 3. Maak een branch

Werk nooit direct op `main`. Maak een branch met een duidelijke naam:

```bash
git checkout -b vis-<naam-van-je-vis>
```

Bijvoorbeeld: `git checkout -b vis-bubbel`.

### 4. Maak je vis

1. Kopieer de voorbeeldvis in de map `fish/`.
2. Geef de kopie de naam van je vis: alleen kleine letters, cijfers en `-`, bijvoorbeeld `fish/goudvis.json`.
3. Pas de waarden aan. Welke keuzes er zijn, zie je in [`shared/options.json`](shared/options.json) en de uitleg in [`shared/README.md`](shared/README.md).

```json
{
  "name": "Goudvis",
  "maker": "Sam",
  "body": "round",
  "fins": "small",
  "pattern": "none",
  "colors": { "body": "#ffaa00", "fins": "#ffffff", "pattern": "#000000" },
  "size": 1.0,
  "speed": 1.0,
  "behavior": "calm"
}
```

> **Privacy:** dit is een openbare repository en dus voor iedereen zichtbaar. Gebruik bij `maker` alleen je voornaam of een bijnaam.

### 5. Controleer je vis

```bash
python tools/validate_fish.py
```

Zie je `Alles klopt!`, dan ben je klaar. Zie je een foutmelding, lees dan wat er staat, pas je bestand aan en probeer het opnieuw.

### 6. Commit en push

```bash
git add fish/goudvis.json
git commit -m "Voeg vis Goudvis toe"
git push -u origin vis-goudvis
```

### 7. Open een pull request

Ga naar je fork op GitHub. Je ziet een knop **Compare & pull request**. Controleer dat je PR gaat **van jouw branch naar `main` van het originele project**. Vul het formulier in en klik op **Create pull request**.

### 8. Verwerk de feedback

- Onder je PR draait een automatische controle. Is die **rood**, klik dan op **Details** om te zien wat er misging. Pas je bestand aan, commit en push opnieuw: je PR wordt vanzelf bijgewerkt.
- Een docent bekijkt je PR. Verwerk de opmerkingen op dezelfde manier.
- Is alles goed, dan wordt je PR gemerged. Je vis zwemt dan in het aquarium.

## Afspraken

- **Eén onderwerp per PR.** Je vis toevoegen en iets anders verbeteren doe je in twee aparte PR's.
- **Duidelijke commitberichten**, bijvoorbeeld `Voeg vis Goudie toe` of `Repareer kleur van vin`.
- **Een issue oppakken?** Reageer eerst op het issue dat jij het gaat doen, zodat niet twee mensen hetzelfde maken.
- **Wees respectvol** in reviews en opmerkingen. Geef opbouwende feedback.

## AI-gebruik

AI-hulp mag, maar je moet je code zelf kunnen uitleggen. Vermeldt in je PR waarvoor je AI hebt gebruikt.

## Je fork bijwerken

Heeft het originele project nieuwe wijzigingen? Klik op GitHub in je fork op **Sync fork** en daarna lokaal:

```bash
git checkout main
git pull
```
