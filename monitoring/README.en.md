<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Lietuvių kalba](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Lithuania only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-23 02:17 UTC, Competition Council: resolutions (kt.gov.lt): 7 addresses read; 0 added, 0 changed, 0 removed; no change; 2 not published, 0 of them with no reason.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Register of Legal Acts (Teisės aktų registras, e-TAR) and its open data](https://www.e-tar.lt) | `konstitucija/`, `kodeksai/`, `istatymai/`, `kiti-aktai/` | — | — | — | not watched yet: not read: www.e-tar.lt and the Seimas's legal acts database (e-seimas.lrs.lt) answer automated requests with a Cloudflare challenge; the Register's open data on data.gov.lt (dataset 2613) refuse this watcher's address by a geographic rule, and the Seimas's open-data services (apps.lrs.lt) do not accept its connections (2026-11-23). The third-party copy of the open data this repository's texts came from (github.com/Yiin/lt-teises-aktai) has not been updated since 2026-08-08. The Constitution is compared with the Seimas's copy, and the laws Lithuania notified to the EU with the acts here (below) |
| [Seimas: the Constitution (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | `konstitucija/` | daily | 2026-11-23 02:17 UTC | no change | watched: the parliament's copy, today's text only; robots.txt asks for 20 s between requests |
| [EU Publications Office (Lithuania's measures transposing EU directives)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | daily | 2026-11-23 02:17 UTC | changes found, flagged | watched: records of the measures only; their texts are in the Register of Legal Acts |
| [EU Publications Office: the laws Lithuania notified (amending laws, consolidated texts)](https://publications.europa.eu/webapi/rdf/sparql) | `kodeksai/`, `istatymai/`, `kiti-aktai/` | daily | 2026-11-23 02:17 UTC | no change | watched: a partial check: only the acts a notification names are compared (laws transposing EU directives); the Register itself is not read (above) |
| [Competition Council: resolutions (kt.gov.lt)](https://kt.gov.lt/lt/teisine-informacija/nutarimai) | `konkurencijos-taryba/` | daily | 2026-11-23 02:17 UTC | no change | watched: decision records (metadata only); the list has no feed or API, so each year is re-read about once a month |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
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
