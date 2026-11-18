# Aquarium

Een interactief aquarium, gebouwd met studenten van Firda Drachten. Ontwerp een eigen vis en voeg die toe via een fork en een pull request. Zo leer je hoe je samenwerkt aan een open-sourceproject op GitHub.

**Bekijk het aquarium:** [firda-software-development-drachten.github.io/aquarium](https://firda-software-development-drachten.github.io/aquarium/)

**Ontwerp je vis:** [de Vissenmaker](https://firda-software-development-drachten.github.io/aquarium/maker/)

Unity 6000.3.27f1 (LTS)

## Hoe werkt het?

1. Je ontwerpt een vis in de **Vissenmaker** en krijgt een visbestand in JSON.
2. Je zet dat bestand in de map `fish/` en opent een **pull request**. Dat kan met de knop **Stuur in via GitHub** in de Vissenmaker, of zelf met een fork, een clone en een branch.
3. Een automatische controle kijkt of je vis klopt. Daarna bekijkt een docent je PR.
4. Na de merge wordt de site opnieuw gebouwd en zwemt je vis in het **Unity-aquarium**.

## Doe mee

Je eerste bijdrage: voeg je eigen vis toe met een fork en een pull request. Er zijn twee routes:

- **Snel:** ontwerp je vis in de [Vissenmaker](https://firda-software-development-drachten.github.io/aquarium/maker/) en klik op **Stuur in via GitHub**. GitHub maakt dan zelf een fork, een branch en een pull request voor je. Je hebt alleen een GitHub-account nodig.
- **Zoals een ontwikkelaar:** fork, clone, maak een branch, commit, push en open een pull request. Zo leer je werken met Git.

Hoe allebei werken, lees je in [CONTRIBUTING.md](CONTRIBUTING.md).

Heb je je eerste vis toegevoegd? Kijk dan bij de [issues](https://github.com/Firda-Software-Development-Drachten/aquarium/issues) voor een volgende taak om op te pakken. Je kunt het Unity-project aanvullen (C#), je kunt de validatie verbeteren (Python) of je kunt aan de Vissenmaker werken (HTML/CSS/JS).

## Wat staat waar?

| Map | Inhoud |
| --- | --- |
| `fish/` | Eén JSON-bestand per vis. Hier komt jouw vis. |
| `shared/` | `options.json`: de lijst met toegestane keuzes voor een vis. Zie [shared/README.md](shared/README.md). |
| `maker/` | De Vissenmaker (HTML, CSS en JavaScript). |
| `tools/` | Python-scripts die vissen controleren en de site bouwen. |
| `webgl/` | De Unity WebGL-build van het aquarium. |

## Zelf controleren

Je hebt alleen Python nodig, geen extra pakketten.

```bash
python tools/validate_fish.py   # klopt mijn vis?
python tools/check_maker.py     # past de Vissenmaker bij options.json?
```

## Hall of Fame
<!-- hall-of-fame:start -->
### Matthijs 
- Billy
- Lemon
### Michael 
- Boris Johnson
### Bram 
- Bram
### Akshay 
- Dark Blue Moon
### fickle 
- fihcle
### IJsbrand 
- Gopher
### Joshua 
- Greeny
### Mourad 
- blob
### Ivan 
- RodeVis
### Silvan 
- Visjuhh
### Firda 
- Voorbeeld
### Yok 
- white
<!-- hall-of-fame:end -->

## Licentie

[MIT](LICENSE)
