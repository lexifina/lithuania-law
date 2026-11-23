<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Stebėsena: kas skaitoma ir kas iš to paaiškėjo

[English](README.en.md)

Kaip global-law stebi visas šalis: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Šis puslapis – tas pats, tik apie šalį: Lietuva. Kiekvienas kartas, kai skaitomas oficialus šaltinis, kada tai įvyko ir kas paaiškėjo (pridėti, pakeisti ir panaikinti aktai). Mašininio skaitymo forma – [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), `git log` – kaip `Kind: check` įrašai (commit), o pagal mėnesius – aplanke [checks/](checks/).

**Paskutinė patikra:** 2026-11-23 02:17 UTC, Konkurencijos taryba: nutarimai (kt.gov.lt): perskaityta adresų: 7; pridėta 0, pakeista 0, panaikinta 0; pakeitimų nėra; neskelbta čia: 2, iš jų be priežasties: 0.

## Šaltiniai

| Šaltinis | Aplankai | Kaip dažnai | Paskutinė sėkminga patikra | Paskutinis rezultatas | Būsena |
| --- | --- | --- | --- | --- | --- |
| [Teisės aktų registras (e-TAR) ir jo atvirieji duomenys](https://www.e-tar.lt) | `konstitucija/`, `kodeksai/`, `istatymai/`, `kiti-aktai/` | — | — | — | dar nestebimas: neskaitomas: www.e-tar.lt ir Seimo teisės aktų duomenų bazė (e-seimas.lrs.lt) į automatines užklausas atsako Cloudflare patikros puslapiu; Registro atvirieji duomenys data.gov.lt (rinkinys 2613) šio stebėtojo adresą atmeta pagal geografinę taisyklę, o Seimo atvirųjų duomenų paslaugos (apps.lrs.lt) jo jungčių nepriima (2026-11-23). Trečiosios šalies atvirųjų duomenų kopija, iš kurios paimti šios repozitorijos tekstai (github.com/Yiin/lt-teises-aktai), neatnaujinta nuo 2026-08-08. Konstitucija lyginama su Seimo kopija, o Lietuvos ES praneštieji įstatymai – su čia esančiais aktais (žr. toliau) |
| [Seimas: Lietuvos Respublikos Konstitucija (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | `konstitucija/` | kasdien | 2026-11-23 02:17 UTC | pakeitimų nėra | stebimas: parlamento kopija, tik dabartinis tekstas; robots.txt prašo 20 s tarp užklausų |
| [ES leidinių biuras (Lietuvos priemonės ES direktyvoms perkelti)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | kasdien | 2026-11-23 02:17 UTC | rasta pakeitimų, pažymėta | stebimas: tik priemonių įrašai; jų tekstai yra Teisės aktų registre |
| [ES leidinių biuras: Lietuvos praneštieji įstatymai (pakeitimo įstatymai, suvestinės redakcijos)](https://publications.europa.eu/webapi/rdf/sparql) | `kodeksai/`, `istatymai/`, `kiti-aktai/` | kasdien | 2026-11-23 02:17 UTC | pakeitimų nėra | stebimas: dalinė patikra: lyginami tik aktai, kuriuos nurodo pranešimai (ES direktyvas perkeliantys įstatymai); pats Registras neskaitomas (žr. aukščiau) |
| [Konkurencijos taryba: nutarimai (kt.gov.lt)](https://kt.gov.lt/lt/teisine-informacija/nutarimai) | `konkurencijos-taryba/` | kasdien | 2026-11-23 02:17 UTC | pakeitimų nėra | stebimas: sprendimų įrašai (tik metaduomenys); sąrašas neturi srauto ar API, todėl kiekvieni metai perskaitomi maždaug kartą per mėnesį |

## Paskutinės 30 dienų

| Pradžia (UTC) | Šaltinis | Perskaityta | Pridėta | Pakeista | Panaikinta | Neskelbta čia (be priežasties) | Rezultatas | Įrašai (commit) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-23 02:17](checks/2026-11.md#lt-kt-nutarimai-20261123t021725z) | kt-nutarimai | 7 | 0 | 0 | 0 | 2 (0) | pakeitimų nėra | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-eu-nim-laws-20261123t021722z) | eu-nim-laws | 1 | 0 | 0 | 0 | 25 (0) | pakeitimų nėra `publish-lag` | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-eu-nim-20261123t021720z) | eu-nim | 1 | 0 | 0 | 0 | 11 (2) | rasta pakeitimų, pažymėta `unexplained-gap` | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-lrs-konstitucija-20261123t021718z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | pakeitimų nėra | — |

## Patikrinkite patys

```
python tools/checktrail.py                      # paskutinė kiekvieno šaltinio patikra
python tools/checktrail.py --day 2026-11-23     # visos tos dienos patikros
python tools/checktrail.py --act <id>           # kada aktas pastebėtas ir paskelbtas čia
git log --grep='^Kind: check' --format='%ci %s'  # patikros istorijoje
```

Teisinę galią turi tik oficialiai paskelbti tekstai (Teisės aktų registras); čia esantys tekstai – kopijos skaitymui ir paieškai.
