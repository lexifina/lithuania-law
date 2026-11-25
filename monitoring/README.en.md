<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Lietuvių kalba](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Lithuania only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-25 05:10 UTC, Competition Council: resolutions (kt.gov.lt): 70 addresses read; 0 added, 12 changed, 0 removed; changes found; 13 not published, 0 of them with no reason. Flags: `verify-differ`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Register of Legal Acts (Teisės aktų registras): open data](https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai) | `konstitucija/`, `kodeksai/`, `istatymai/`, `kiti-aktai/` | daily | 2026-11-25 05:07 UTC | no change | watched: read through an EU address: data.gov.lt refuses this watcher's own by a geographic rule. www.e-tar.lt and e-seimas.lrs.lt answer automated requests with a Cloudflare challenge and are not read |
| [Seimas: the Constitution (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | `konstitucija/` | daily | 2026-11-25 05:07 UTC | no change | watched: a second check of the Constitution: the parliament's copy, today's text only; robots.txt asks for 20 s between requests |
| [EU Publications Office (Lithuania's measures transposing EU directives)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | daily | 2026-11-25 05:07 UTC | no change | watched: records of the measures only; their texts are in the Register of Legal Acts |
| [EU Publications Office: the laws Lithuania notified (amending laws, consolidated texts)](https://publications.europa.eu/webapi/rdf/sparql) | `kodeksai/`, `istatymai/`, `kiti-aktai/` | daily | 2026-11-25 05:07 UTC | no change | watched: a second check beside the Register: only the acts a notification names are compared (laws transposing EU directives), and they are not counted again in the freshness totals |
| [Competition Council: resolutions (kt.gov.lt)](https://kt.gov.lt/lt/teisine-informacija/nutarimai) | `konkurencijos-taryba/` | daily | 2026-11-25 05:10 UTC | changes found | watched: decision records (metadata only); the list has no feed or API, so each year is re-read about once a month |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-25 05:07](checks/2026-11.md#lt-kt-nutarimai-20261125t050752z) | kt-nutarimai | 70 | 0 | 12 | 0 | 13 (0) | changes found `verify-differ` | [250](https://github.com/lexifina/lithuania-law/compare/f8785592b097...1512130cbab0) |
| [2026-11-25 05:07](checks/2026-11.md#lt-eu-nim-laws-20261125t050750z) | eu-nim-laws | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-25 05:07](checks/2026-11.md#lt-eu-nim-20261125t050704z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | no change | — |
| [2026-11-25 05:07](checks/2026-11.md#lt-lrs-konstitucija-20261125t050701z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-25 05:02](checks/2026-11.md#lt-tar-20261125t050203z) | tar | 59 | 0 | 0 | 0 | 16 (0) | no change `audit-disagrees` | — |
| [2026-11-24 08:04](checks/2026-11.md#lt-lrs-konstitucija-20261124t080402z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-24 05:17](checks/2026-11.md#lt-kt-nutarimai-20261124t051737z) | kt-nutarimai | 59 | 0 | 0 | 0 | 12 (0) | no change `verify-differ` | — |
| [2026-11-24 05:17](checks/2026-11.md#lt-eu-nim-laws-20261124t051736z) | eu-nim-laws | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-24 05:16](checks/2026-11.md#lt-eu-nim-20261124t051650z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | no change | — |
| [2026-11-24 05:15](checks/2026-11.md#lt-lrs-konstitucija-20261124t051546z) | lrs-konstitucija | 4 | 0 | 0 | 0 | 0 (0) | the source did not answer | — |
| [2026-11-24 05:11](checks/2026-11.md#lt-tar-20261124t051117z) | tar | 53 | 0 | 0 | 0 | 16 (0) | no change `audit-disagrees` | — |
| [2026-11-23 23:26](checks/2026-11.md#lt-kt-nutarimai-20261123t232634z) | kt-nutarimai | 46 | 0 | 0 | 0 | 9 (0) | no change | — |
| [2026-11-23 23:26](checks/2026-11.md#lt-eu-nim-laws-20261123t232632z) | eu-nim-laws | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 23:25](checks/2026-11.md#lt-eu-nim-20261123t232543z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | no change | — |
| [2026-11-23 23:25](checks/2026-11.md#lt-lrs-konstitucija-20261123t232541z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 23:23](checks/2026-11.md#lt-tar-20261123t232342z) | tar | 23 | 0 | 0 | 0 | 16 (0) | no change | — |
| [2026-11-23 23:20](checks/2026-11.md#lt-kt-nutarimai-20261123t232043z) | kt-nutarimai | 35 | 0 | 0 | 0 | 7 (0) | no change | — |
| [2026-11-23 23:20](checks/2026-11.md#lt-eu-nim-laws-20261123t232041z) | eu-nim-laws | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 23:19](checks/2026-11.md#lt-eu-nim-20261123t231953z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | no change | — |
| [2026-11-23 23:19](checks/2026-11.md#lt-lrs-konstitucija-20261123t231951z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 23:15](checks/2026-11.md#lt-tar-20261123t231540z) | tar | 30 | 1 | 24 | 0 | 20 (0) | changes found `verify-differ` `audit-disagrees` | [235](https://github.com/lexifina/lithuania-law/compare/07eb86ea70a3...3911574bee11) |
| [2026-11-23 23:10](checks/2026-11.md#lt-kt-nutarimai-20261123t231029z) | kt-nutarimai | 33 | 0 | 0 | 0 | 4 (0) | changes found | [2](https://github.com/lexifina/lithuania-law/compare/7340dbde4fe8...6ca44fbb4e01) |
| [2026-11-23 23:10](checks/2026-11.md#lt-eu-nim-laws-20261123t231024z) | eu-nim-laws | 1 | 23 | 0 | 0 | 0 (0) | changes found `verify-differ` | — |
| [2026-11-23 23:09](checks/2026-11.md#lt-eu-nim-20261123t230925z) | eu-nim | 17 | 0 | 0 | 0 | 3 (0) | changes found | [9](https://github.com/lexifina/lithuania-law/compare/4688ee57ffe8...7340dbde4fe8) |
| [2026-11-23 23:09](checks/2026-11.md#lt-lrs-konstitucija-20261123t230923z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 22:53](checks/2026-11.md#lt-tar-20261123t225355z) | tar | 169 | 0 | 0 | 0 | 92 (0) | changes found `verify-differ` `audit-disagrees` | [1388](https://github.com/lexifina/lithuania-law/compare/030078693038...4688ee57ffe8) |
| [2026-11-23 02:36](checks/2026-11.md#lt-kt-nutarimai-20261123t023630z) | kt-nutarimai | 5 | 0 | 0 | 0 | 5 (3) | changes found, flagged `unexplained-gap` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-eu-nim-laws-20261123t023628z) | eu-nim-laws | 1 | 0 | 0 | 0 | 25 (0) | no change `publish-lag` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-eu-nim-20261123t023626z) | eu-nim | 1 | 0 | 0 | 0 | 11 (2) | changes found, flagged `unexplained-gap` | — |
| [2026-11-23 02:36](checks/2026-11.md#lt-lrs-konstitucija-20261123t023625z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 02:34](checks/2026-11.md#lt-tar-20261123t023445z) | tar | 20 | 0 | 0 | 0 | 253 (34) | changes found, flagged `publish-lag` `unexplained-gap` | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-kt-nutarimai-20261123t021725z) | kt-nutarimai | 7 | 0 | 0 | 0 | 2 (0) | no change | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-eu-nim-laws-20261123t021722z) | eu-nim-laws | 1 | 0 | 0 | 0 | 25 (0) | no change `publish-lag` | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-eu-nim-20261123t021720z) | eu-nim | 1 | 0 | 0 | 0 | 11 (2) | changes found, flagged `unexplained-gap` | — |
| [2026-11-23 02:17](checks/2026-11.md#lt-lrs-konstitucija-20261123t021718z) | lrs-konstitucija | 1 | 0 | 0 | 0 | 0 (0) | no change | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
