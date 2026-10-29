# How this repository was made (Lithuania)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Teisės aktų registras (Register of Legal Acts, www.e-tar.lt), via the Internet Archive | <https://www.e-tar.lt> | 2026-10-29 | Legal acts are not objects of copyright (Law on Copyright and Related Rights, art. 5); Internet Archive Wayback Machine captures, pinned by timestamp |
| Lietuvos Respublikos Seimas: Lietuvos Respublikos Konstitucija (www.lrs.lt) | <https://www.lrs.lt/home/Konstitucija/Konstitucija.htm> | 2026-10-29 | Legal acts are not objects of copyright (Law on Copyright and Related Rights, art. 5) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `konstitucija` | Lietuvos Respublikos Konstitucija | 12 | 1992-11-02 to 2022-05-22 |

The build made 16 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 15 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `ateitis`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 16 laws in the record.
- 28 tags.

## Dates

Each commit is dated at noon (Europe/Vilnius) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Konstitucija art. 149(3): a law amending the Constitution takes effect no earlier than one month after its adoption; art. 70(2): other laws take effect after signature and official publication, unless they set a later day. The in-force day of each version here is the one the Register of Legal Acts gives its consolidated edition. https://www.e-tar.lt/portal/lt/legalAct/TAR.47BB952431DA

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `abce83923fa47fe3859c7a7099dba4ded720a2a188e53d947d89bd9af4b8b647` (865208 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

12 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Lithuanian, the official language, as the Register of Legal Acts (e-TAR) prints it. The README is in English first.
- e-TAR texts come from pinned Internet Archive captures.
- In-force days are the start dates e-TAR gives its consolidated editions ("Suvestinė redakcija nuo"). No constitutional amendment sets its own day; Art. 149(3) only says not earlier than one month after adoption.
- Version 1 is e-TAR's text of the Constitution as adopted (rs/legalact), capture of 2018-06-26. The 2015 capture of the same page reads "KONSTITUCIJA" for "KONSTITUCIJĄ" in the preamble and the 2017 capture adds a comma in Art. 7; both are transcription slips the Register later corrected, and every consolidated text agrees with the 2018 capture.
- e-TAR's consolidated editions from 1996-07-21 to 2013-11-16 are in no archive, so those versions replay each amending law's own words (e-TAR rs/legalact) on the version before: I-1390 (Art. 47 part 2 inserted), VIII-32 and IX-959 (Art. 119(2) restated), IX-1305 (Art. 47), IX-1378 (Art. 84 point 11), IX-1379 (Art. 118), IX-2343 (Art. 150 and the EU membership Constitutional Act), IX-2344 (Art. 57), X-572 (Art. 125). Each rule asserts the law's operative words, and the result is checked against lrs.lt (2006) and e-TAR's 2014 edition (see the checks).
- Law IX-1378 restates Art. 84 point 11 ending with a full stop; e-TAR and lrs.lt print it with the semicolon that ends every point of the list, and so does this record.
- Where two or more laws took effect on one day (2003-04-21, 2004-08-14, 2022-05-22), each article is credited to the law that e-TAR's note under it names ("Straipsnio pakeitimas: Nr. …").
- The 2013 notice of the President of the Constitutional Court (suspension of Law X-572) and ruling KT2-N1/2014 changed no words; they are versions without units, credited to Art. 125. Their kinds are court.
- Units: the preamble (with the referendum line), the 15 chapter headings (I-XIV skirsnis and Baigiamieji nuostatai), the 154 articles, and from 2004 the Constitutional Act "Dėl Lietuvos Respublikos narystės Europos Sąjungoje", added to the Constitution by Law IX-2343 art. 1 and printed among its component parts by lrs.lt (e-TAR's consolidated text lists it in Art. 150 but does not print it). The three component parts of 1991-1992 (Art. 150) are separate acts and not included.
- Left out of the units: the title lines (in the act title), the 1992 signature block, e-TAR's notes under articles ("Straipsnio pakeitimas", "TAR pastaba") and its change list.
- Typesetting normalised once (lt_common.norm): spaces, straight and curly double quotes to „…“, a spaced hyphen to an en dash, soft hyphens dropped. On lrs.lt a <br> ends a paragraph.
- Check: e-TAR original text, capture 20150405020457 against 20180626074019: differs only in preambule
- Check: e-TAR original text, capture 20170610031037 against 20180626074019: differs only in art-007, preambule
- Check: 1996-07-21: I-1390 -> art-047
- Check: 1997-01-13: VIII-32 -> art-119
- Check: 2002-07-21: IX-959 -> art-119
- Check: 2003-02-24: IX-1305 -> art-047
- Check: 2003-04-21: IX-1378, IX-1379 -> art-084, art-118
- Check: 2004-08-14: IX-2343, IX-2344 -> art-057, art-150, sudedamoji-4-es
- Check: 2006-05-26: X-572 -> art-125
- Check: 2013-11-16: PRANESIMAS-2013 -> art-125 (wording unchanged)
- Check: 2014-01-24: KT2-N1/2014 -> art-125 (wording unchanged)
- Check: 2019-09-01: XIII-2004 -> art-106, art-107
- Check: 2022-05-22: XIV-1028, XIV-1029, XIV-1030 -> art-056, art-067, art-074, art-119, art-122, art-124, art-141, art-143
- Check: replayed text in force 2004-08-14..2006-05-25 vs lrs.lt (Jan 2006): identical in all 170 units
- Check: text in force 2007-11-15 vs lrs.lt capture 20071115210902: identical in all 170 units
- Check: text in force 2008-10-31 vs lrs.lt capture 20081031163054: identical in all 170 units
- Check: text in force 2014-02-08 vs lrs.lt capture 20140208101040: identical in all 170 units
- Check: text in force 2016-06-10 vs lrs.lt capture 20160610034218: identical in all 170 units
- Check: text in force 2020-11-13 vs lrs.lt capture 20201113085724: identical in all 170 units
- Check: text in force 2026-10-20 vs lrs.lt capture 20261020031657: identical in all 170 units
- Check: text in force 2019-09-01..2022-05-21 vs lrs.lt capture 20220627033621 (the page lagged the 2022-05-22 edition): identical in all 170 units
- Check: replayed text in force 2006-05-26 vs e-TAR 2014-01-24 edition: identical in all 170 units
- Check: e-TAR edition from 2014-01-24, capture 20160916065801: differs only in preambule
- Check: e-TAR edition from 2014-01-24, capture 20181025085204: differs only in nothing
- Check: e-TAR edition from 2019-09-01, capture 20210227025534: differs only in nothing
- Check: text in force today vs lrs.lt as served 2026-10-29: identical in all 170 units
- Check: EU membership Constitutional Act (from Law IX-2343) vs lrs.lt 2026-10-29: identical
- Check: e-TAR act page captured 20261023174812 names the edition in force from 2022-05-22; the newest version here is from 2022-05-22

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code and chose the sources. No model wrote or altered legal text: every unit is the publisher's text or the amending law's own words, applied by code, and the commit notes for the 2013 notice and the 2014 ruling paraphrase those documents in English (2 notes).
