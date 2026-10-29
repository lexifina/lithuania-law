"""The 1992 Constitution: split a text (e-TAR original, e-TAR consolidated edition, or the Seimas lrs.lt page) into
units, and replay the amending laws whose consolidated edition no archive holds."""
import re

ROMAN = {r: i for i, r in enumerate(
    'I II III IV V VI VII VIII IX X XI XII XIII XIV XV'.split(), 1)}
ART = re.compile(r'^(\d{1,3}) straipsnis$')
SKIRSNIS = re.compile(r'^([IVX]+) SKIRSNIS$')
NOTE_HEAD = re.compile(r'^(Straipsnio|Straipsnio dalies|Straipsnio punkto|Preambulės)? ?(pakeitimai|pakeitimas|papildymas|papildymai):?$', re.I)
LAWNO = re.compile(r'Nr\. ([IVX]+-\d+)')
TAR_NOTE = 'TAR pastaba.'


def split(paras: list[str], kind: str) -> tuple[dict, dict]:
    """Units {key: {'label','kind','text'}} and per-unit amendment notes {key: [law numbers]} (consolidated texts
    print them after each article; the original has none). `kind` is 'tar' or 'lrs'."""
    # where the body starts: the title
    start = next(i for i, p in enumerate(paras) if p in ('LIETUVOS RESPUBLIKOS', 'LIETUVOS RESPUBLIKOS KONSTITUCIJA'))
    units, notes, order = {}, {}, []
    cur = None
    buf: list[str] = []
    in_note = False
    pending_head = None

    def flush():
        nonlocal buf
        if cur is not None:
            units[cur]['lines'] = buf
        buf = []

    def new(key, label, kind_, head):
        nonlocal cur, in_note
        flush()
        cur = key
        in_note = False
        units[key] = {'label': label, 'kind': kind_, 'head': head}
        order.append(key)
        notes.setdefault(key, [])

    i = start
    n = len(paras)
    new('preambule', 'Preambulė', 'preamble', None)
    while i < n:
        p = paras[i]
        if p == 'LIETUVOS RESPUBLIKOS' and i + 2 < n and paras[i + 1] == 'AUKŠČIAUSIOSIOS TARYBOS':
            break  # the 1992 signature block; the consolidated text's change list follows it
        if p.startswith('LIETUVOS RESPUBLIKOS AUKŠČIAUSIOSIOS TARYBOS PIRMININKAS'):
            break
        m = SKIRSNIS.match(p)
        if m and i + 1 < n:
            num = ROMAN[m.group(1)]
            new(f'skirsnis-{num:02d}', f'{m.group(1)} skirsnis', 'chapter', f'# {p}')
            buf.append(paras[i + 1])
            i += 2
            continue
        if p == 'BAIGIAMIEJI NUOSTATAI':
            new('skirsnis-15', 'Baigiamieji nuostatai', 'chapter', f'# {p}')
            i += 1
            continue
        m = ART.match(p)
        if m:
            num = int(m.group(1))
            new(f'art-{num:03d}', f'{num} straipsnis', 'art', f'# {p}')
            i += 1
            continue
        if NOTE_HEAD.match(p) or p.startswith('Straipsnio pakeitim') or p.startswith('Straipsnio dalies pakeitim'):
            in_note = True
            rest = p.split(':', 1)[1] if ':' in p else ''
            notes[cur] += LAWNO.findall(rest)
            i += 1
            continue
        if p.startswith(TAR_NOTE) or p.startswith('Pastaba.'):
            in_note = True
            i += 1
            continue
        if in_note:
            if re.match(r'^(Nr\. |\d{4}-\d{2}-\d{2}, Žin)', p):
                notes[cur] += LAWNO.findall(p)
                i += 1
                continue
            in_note = False
        buf.append(p)
        i += 1
    flush()
    out = {}
    for k in order:
        u = units[k]
        lines = u['lines']
        if k == 'preambule':
            lines = [l for l in lines]
        text = '\n'.join(([u['head']] if u['head'] else []) + lines) + '\n'
        out[k] = {'label': u['label'], 'kind': u['kind'], 'text': text}
    return out, notes


def body(unit: dict) -> list[str]:
    """The paragraphs of a unit without its heading line."""
    lines = unit['text'].rstrip('\n').split('\n')
    return lines[1:] if lines[0].startswith('# ') else lines


def make(key: str, label: str, kind: str, head: str | None, lines: list[str]) -> dict:
    return {'label': label, 'kind': kind, 'text': '\n'.join(([head] if head else []) + lines) + '\n'}


def quoted(paras: list[str]) -> list[list[str]]:
    """The quoted blocks of an amending law: runs of paragraphs from one opening „ to its closing “."""
    out, cur = [], None
    for p in paras:
        if cur is None and p.startswith('„'):
            cur = [p[1:]]
        elif cur is not None:
            cur.append(p)
        else:
            continue
        if cur and cur[-1].endswith('“'):
            cur[-1] = cur[-1][:-1]
            out.append(cur)
            cur = None
    return out
