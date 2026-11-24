<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for Lithuania

[Lietuvių kalba](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for Lithuania only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [Register of Legal Acts (Teisės aktų registras): open data](https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai) | the Register's open data (data.gov.lt dataset 2613, its API): the list of every law, code and constitutional act with its number, status and days (one request, only the fields needed), and the consolidated editions of every act held here (50 acts a request), 5 s between requests | `konstitucija/`, `kodeksai/`, `istatymai/`, `kiti-aktai/` | daily | 2026-11-24 05:11 UTC | watched: read through an EU address: data.gov.lt refuses this watcher's own by a geographic rule. www.e-tar.lt and e-seimas.lrs.lt answer automated requests with a Cloudflare challenge and are not read |
| [Seimas: the Constitution (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | the Seimas's consolidated text of the Constitution (one page): the amending laws its notes name, the day the page last changed and a fingerprint of its text | `konstitucija/` | daily | 2026-11-24 05:15 UTC | watched: a second check of the Constitution: the parliament's copy, today's text only; robots.txt asks for 20 s between requests |
| [EU Publications Office (Lithuania's measures transposing EU directives)](https://publications.europa.eu/webapi/rdf/sparql) | every national implementing measure Lithuania notified, with its notification day, entry-into-force day and the day the record last changed (one SPARQL query a run) | `eu-nim/` | daily | 2026-11-24 05:16 UTC | watched: records of the measures only; their texts are in the Register of Legal Acts |
| [EU Publications Office: the laws Lithuania notified (amending laws, consolidated texts)](https://publications.europa.eu/webapi/rdf/sparql) | the same list (read once a run): each notified law and code with its number, title and entry-into-force day; the amending laws, repeals and consolidated texts it names are compared with the laws, codes and other acts held here | `kodeksai/`, `istatymai/`, `kiti-aktai/` | daily | 2026-11-24 05:17 UTC | watched: a second check beside the Register: only the acts a notification names are compared (laws transposing EU directives), and they are not counted again in the freshness totals |
| [Competition Council: resolutions (kt.gov.lt)](https://kt.gov.lt/lt/teisine-informacija/nutarimai) | the Council's list of resolutions (12 a page): its newest page with the list's total, and every page of one year per check, a year after another: day, number, day published and document | `konkurencijos-taryba/` | daily | 2026-11-24 05:17 UTC | watched: decision records (metadata only); the list has no feed or API, so each year is re-read about once a month |

Sources are read within their robots.txt and terms, with pauses between requests.
