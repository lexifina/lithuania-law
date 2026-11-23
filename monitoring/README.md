<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Stebėsena: kas skaitoma ir kas iš to paaiškėjo

[English](README.en.md)

Kaip global-law stebi visas šalis: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Šis puslapis – tas pats, tik apie šalį: Lietuva. Kiekvienas kartas, kai skaitomas oficialus šaltinis, kada tai įvyko ir kas paaiškėjo (pridėti, pakeisti ir panaikinti aktai). Mašininio skaitymo forma – [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), `git log` – kaip `Kind: check` įrašai (commit), o pagal mėnesius – aplanke [checks/](checks/).

**Paskutinė patikra:** 2026-11-23 23:21 UTC, Konkurencijos taryba: nutarimai (kt.gov.lt): perskaityta adresų: 35; pridėta 0, pakeista 0, panaikinta 0; pakeitimų nėra; neskelbta čia: 7, iš jų be priežasties: 0.

## Šaltiniai

| Šaltinis | Aplankai | Kaip dažnai | Paskutinė sėkminga patikra | Paskutinis rezultatas | Būsena |
| --- | --- | --- | --- | --- | --- |
| [Teisės aktų registras: atvirieji duomenys](https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai) | `konstitucija/`, `kodeksai/`, `istatymai/`, `kiti-aktai/` | kasdien | 2026-11-23 23:19 UTC | rasta pakeitimų | stebimas: skaitoma per ES adresą: data.gov.lt pagal geografinę taisyklę atmeta paties stebėtojo adresą. www.e-tar.lt ir e-seimas.lrs.lt į automatines užklausas atsako Cloudflare patikros puslapiu ir neskaitomi |
| [Seimas: Lietuvos Respublikos Konstitucija (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | `konstitucija/` | kasdien | 2026-11-23 23:19 UTC | pakeitimų nėra | stebimas: antra Konstitucijos patikra: parlamento kopija, tik dabartinis tekstas; robots.txt prašo 20 s tarp užklausų |
| [ES leidinių biuras (Lietuvos priemonės ES direktyvoms perkelti)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | kasdien | 2026-11-23 23:20 UTC | pakeitimų nėra | stebimas: tik priemonių įrašai; jų tekstai yra Teisės aktų registre |
| [ES leidinių biuras: Lietuvos praneštieji įstatymai (pakeitimo įstatymai, suvestinės redakcijos)](https://publications.europa.eu/webapi/rdf/sparql) | `kodeksai/`, `istatymai/`, `kiti-aktai/` | kasdien | 2026-11-23 23:20 UTC | pakeitimų nėra | stebimas: antra patikra greta Registro: lyginami tik aktai, kuriuos nurodo pranešimai (ES direktyvas perkeliantys įstatymai), ir jie dar kartą neskaičiuojami aktualumo sumose |
| [Konkurencijos taryba: nutarimai (kt.gov.lt)](https://kt.gov.lt/lt/teisine-informacija/nutarimai) | `konkurencijos-taryba/` | kasdien | 2026-11-23 23:21 UTC | pakeitimų nėra | stebimas: sprendimų įrašai (tik metaduomenys); sąrašas neturi srauto ar API, todėl kiekvieni metai perskaitomi maždaug kartą per mėnesį |

## Paskutinės 30 dienų

| Pradžia (UTC) | Šaltinis | Perskaityta | Pridėta | Pakeista | Panaikinta | Neskelbta čia (be priežasties) | Rezultatas | Įrašai (commit) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-23 23:20](checks/2026-11.md#lt-kt-nutarimai-20261123t232043z) | kt-nutarimai | 35 | 0 | 0 | 0 | 7 (0) | pakeitimų nėra | — |
| [2026-11-23 23:20](checks/2026-11.md#lt-eu-nim-laws-20261123t232041z) | eu-nim-laws | 1 | 0 | 0 | 0 | 0 (0) | pakeitimų nėra | — |
| [2026-11-23 23:19](checks/2026-11.md#lt-eu-nim-20261123t231953z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | pakeitimų nėra | — |
| [2026-11-23 23:19](checks/2026-11.md#lt-lrs-konstitucija-20261123t231951z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | pakeitimų nėra | — |
| [2026-11-23 23:15](checks/2026-11.md#lt-tar-20261123t231540z) | tar | 30 | 1 | 24 | 0 | 20 (0) | rasta pakeitimų `verify-differ` `audit-disagrees` | [235](https://github.com/lexifina/lithuania-law/compare/07eb86ea70a3...3911574bee11) |
| [2026-11-23 23:10](checks/2026-11.md#lt-kt-nutarimai-20261123t231029z) | kt-nutarimai | 33 | 0 | 0 | 0 | 4 (0) | rasta pakeitimų | [2](https://github.com/lexifina/lithuania-law/compare/7340dbde4fe8...6ca44fbb4e01) |
| [2026-11-23 23:10](checks/2026-11.md#lt-eu-nim-laws-20261123t231024z) | eu-nim-laws | 1 | 23 | 0 | 0 | 0 (0) | rasta pakeitimų `verify-differ` | — |
| [2026-11-23 23:09](checks/2026-11.md#lt-eu-nim-20261123t230925z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | rasta pakeitimų | [9](https://github.com/lexifina/lithuania-law/compare/4688ee57ffe8...7340dbde4fe8) |
| [2026-11-23 23:09](checks/2026-11.md#lt-lrs-konstitucija-20261123t230923z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | pakeitimų nėra | — |
| [2026-11-23 22:53](checks/2026-11.md#lt-tar-20261123t225355z) | tar | 169 | 0 | 0 | 0 | 92 (0) | rasta pakeitimų `verify-differ` `audit-disagrees` | [1388](https://github.com/lexifina/lithuania-law/compare/030078693038...4688ee57ffe8) |
| [2026-11-23 02:36](checks/2026-11.md#lt-kt-nutarimai-20261123t023630z) | kt-nutarimai | 5 | 0 | 0 | 0 | 5 (3) | rasta pakeitimų, pažymėta `unexplained-gap` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-eu-nim-laws-20261123t023628z) | eu-nim-laws | 1 | 0 | 0 | 0 | 25 (0) | pakeitimų nėra `publish-lag` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-eu-nim-20261123t023626z) | eu-nim | 1 | 0 | 0 | 0 | 11 (2) | rasta pakeitimų, pažymėta `unexplained-gap` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-lrs-konstitucija-20261123t023625z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | pakeitimų nėra | — |
| [2026-11-23 02:34](checks/2026-11.md#lt-tar-20261123t023445z) | tar | 20 | 0 | 0 | 0 | 253 (34) | rasta pakeitimų, pažymėta `publish-lag` `unexplained-gap` | — |
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
