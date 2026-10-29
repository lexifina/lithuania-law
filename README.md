# Lithuania: law history in git

The law of the Republic of Lithuania as a git history: one file per provision, one commit per change on the day it took effect, and the law or court document that made each change as the commit's author. `git blame` names the act behind a paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lt/`. The texts are in Lithuanian (lietuvių kalba), the official language, as the Register of Legal Acts (Teisės aktų registras, e-TAR) prints them.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `konstitucija/` | Lietuvos Respublikos Konstitucija (the Constitution adopted by referendum on 25 October 1992) | 12 | Complete: the text as adopted (in force 2 November 1992) and every change since, from Law I-1390 (1996) to Laws XIV-1028, XIV-1029 and XIV-1030 (in force 22 May 2022) |

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did Article 119 say on 1 January 2000? | `python tools/on.py 2000-01-01 konstitucija art-119` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2000-01-01T23:59:59Z" main -- konstitucija/art-119.md):konstitucija/art-119.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2000-01-01T23:59:59Z" main -- konstitucija/art-119.md; git show "$($r):konstitucija/art-119.md"` |
| Who wrote each paragraph of Article 47 (land ownership)? | `git blame konstitucija/art-047.md` |
| Every change to Article 119 (local government), word by word | `git log -p --word-diff konstitucija/art-119.md` |
| Every change in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything Law XIV-1028 (direct election of mayors) changed | `git log --author="XIV-1028" --stat` |
| The whole Constitution on a date | `python tools/on.py 2010-01-01 konstitucija` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Vilnius, on the day the change took effect**. The adoption and publication dates are trailers; the in-force day is in `In-force:`, which `tools/on.py` reads.
- **The in-force day of every version is the one the Register of Legal Acts gives its consolidated edition** ("Suvestinė redakcija nuo …"). A law amending the Constitution takes effect no earlier than one month after its adoption (Art. 149(3)); none of these laws names a day of its own.
- **The Constitution** was adopted by referendum on 25 October 1992 and took effect on 2 November 1992.
- **16 November 2013** and **24 January 2014** change no words (see below); their commits say "wording unchanged".
- `--before="YYYY-MM-DD"` alone uses your clock's time of day; use `T23:59:59Z` as above, or the tool.

## How it is checked

- **1992 and 2014-2022 are the Register's own texts**: the Constitution as adopted (e-TAR `rs/legalact`) and its consolidated editions in force from 24 January 2014, 1 September 2019 and 22 May 2022 (e-TAR `rs/actualedition`), each read from a pinned Internet Archive capture.
- **1996-2006 replay the amending laws.** The Register's consolidated editions for those years are in no archive, so each version applies the amending law's own words (its e-TAR text) to the version before it. Each rule checks the law's operative words ("Pakeisti 119 straipsnio 2 dalį ir ją išdėstyti taip: …") and stops the build if they differ.
- **Every version is checked against the Seimas's own copy** of the Constitution (lrs.lt): the replayed text in force from 14 August 2004 equals the lrs.lt page archived in January 2006 in all 170 units, and the text in force from 26 May 2006 equals the Register's 2014 edition and the lrs.lt pages of 2007, 2008, 2014 and 2016. The 2019 text equals lrs.lt in 2020, and today's text equals lrs.lt as served on 29 October 2026 and as archived on 20 October 2026. The Register's act page (archived 23 October 2026) names the edition from 22 May 2022 as the one in force.
- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing is dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- The repository is rebuilt a second time from the same data and must give identical hashes.

## What "author" means

The author of a commit is the act that made the change, with an e-mail address that cannot exist (`xiv-1028@e-tar.invalid`), so `git blame` and `git log --author` name it. The committer is always Lexifina.

- **The first commit** is the Constitution as adopted by the referendum of 25 October 1992.
- **Credits come only from the sources.** Each version is credited to the laws the Register lists for that edition. Where several laws took effect on one day (21 April 2003, 14 August 2004, 22 May 2022), each article is credited to the law the Register's note under it names ("Straipsnio pakeitimas: Nr. …").
- **The Article 125 story.** Law X-572 (2006) removed the Bank of Lithuania's exclusive right to issue money (Art. 125(2)). On 16 November 2013 the President of the Constitutional Court gave notice that the law was suspended while the Court examined it, and ruling KT2-N1/2014 of 24 January 2014 held that it had been adopted contrary to Art. 147(1). From then on the law, including the new Art. 125(2), may not be applied, but the earlier wording does not return. The Register keeps printing the 2006 words with a note, and so does this record: the notice and the ruling are commits that change no words.
- Blame credits whole lines (one paragraph or point per line); use `git log -p --word-diff` for the words.

## What it does not show

- **The Register's own consolidated editions for 1996-2013**: those versions are the amending laws applied by code, checked against the Seimas's 2006-2008 pages (see above). One adjustment follows the consolidated texts rather than the law: Law IX-1378 ends the restated Art. 84 point 11 with a full stop, where every consolidated text keeps the list's semicolon.
- **The three component parts of 1991-1992** that Art. 150 lists (the Constitutional Law "Dėl Lietuvos valstybės", the Constitutional Act on non-alignment with post-Soviet eastern unions, and the Law on the procedure for the entry into force of the Constitution). They are separate acts. The fourth component part, the Constitutional Act on membership of the European Union (2004), is included (`konstitucija/sudedamoji-4-es.md`), from Law IX-2343 itself.
- **Ordinary laws and codes.** The Civil Code, the Criminal Code and the Law on the Legal Protection of Personal Data are not built yet: the Register blocks automated readers, its open-data API (data.gov.lt) is closed to this build, and the archives hold only some of these acts' many editions.
- **Rejected amendments.** Proposals that failed in the Seimas or at a referendum changed no words and are not recorded.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

No OCR was run, and no AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions by date | Names the amending act | API or bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Register of Legal Acts (e-TAR)](https://www.e-tar.lt) via the [Internet Archive](https://web.archive.org/) | Official publication | yes (consolidated editions with dates) | yes, per article | – | – |
| [Register open data (data.gov.lt, dataset 2613)](https://data.gov.lt/datasets/2613/) | Official open data (acts, texts, consolidated versions) | yes | partly | yes (Spinta API) | – |
| [Seimas: the Constitution (lrs.lt)](https://www.lrs.lt/home/Konstitucija/Konstitucija.htm) | The parliament's consolidated copy | current only (archived 2006-2026) | yes, per article | no | – |
| [e-seimas.lrs.lt](https://e-seimas.lrs.lt) | Seimas legal database | yes | yes | no | – |
| [lt-teises-aktai](https://github.com/Yiin/lt-teises-aktai) | Volunteer git history from e-TAR | yes | partly | n/a | Prior art only; nothing copied |
| [legalize-lt](https://github.com/legalize-dev/legalize-lt) | Reconstructed history from e-TAR (data CC BY 4.0) | yes | partly | git | Checked, not used: at commit 76c1b579 its text of the personal data law (2025-01-01) is not e-TAR's edition (repealed articles kept, articles 7¹, 14¹, 19¹, 32¹ missing, superscripts lost) |

Research guides: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

Legal acts are not objects of copyright in Lithuania (Law on Copyright and Related Rights, art. 5). The texts come from the Register of Legal Acts (www.e-tar.lt, read through the Internet Archive) and were checked against the Seimas's copy (www.lrs.lt). Lexifina's own contributions are dedicated to the public domain under CC0 1.0; see `LICENSE`.

This repository is not legal advice and is not an official publication.

---

## Lietuviškai

Lietuvos Respublikos Konstitucija kaip istorija git sistemoje: kiekvienam straipsniui atskiras failas ir kiekvienam pakeitimui atskiras įrašas (commit), datuotas jo įsigaliojimo diena, o autorius yra pakeitimą padaręs teisės aktas. Istorija prasideda 1992 m. spalio 25 d. referendumu priimtu tekstu (įsigaliojo 1992 m. lapkričio 2 d.) ir apima visus pakeitimus iki 2022 m. gegužės 22 d. įsigaliojusių įstatymų Nr. XIV-1028, XIV-1029 ir XIV-1030. Tekstai paimti iš Teisės aktų registro (per Interneto archyvą) ir sutikrinti su Seimo svetainėje skelbiamu Konstitucijos tekstu. Tai nėra oficiali suvestinė redakcija ir ne teisinė konsultacija.
