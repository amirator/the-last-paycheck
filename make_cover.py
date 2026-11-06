"""Front ebook cover (1600x2560) + full paperback wrap for The Last Paycheck."""
from PIL import Image, ImageDraw, ImageFont

INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
ACCENT = (255, 90, 31)
BG = (17, 18, 20)
INK = (240, 238, 234)
GREY = (150, 150, 152)

def F(weight, size):
    return ImageFont.truetype(INTER.format(weight), size)

def center(d, y, text, font, fill, W, ls=0):
    if ls:
        text = (" " * 1).join(text)  # cheap letterspacing via spaces when ls=1
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)
    return y + font.size

def slope_motif(d, x0, y0, w, h, lw):
    """The book's signature motif: one grey line rises, the accent line falls."""
    import math
    d.line([(x0, y0), (x0 + w, y0 - h * 0.42)], fill=(90, 90, 94), width=lw)
    d.line([(x0, y0), (x0 + w, y0 + h * 0.58)], fill=ACCENT, width=lw + 2)
    r = lw * 1.6
    for (cx, cy, col) in [(x0, y0, INK), (x0 + w, y0 - h * 0.42, (90, 90, 94)),
                          (x0 + w, y0 + h * 0.58, ACCENT)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

def draw_front(d, W, H, ox=0):
    # top kicker
    k = F("SemiBold", 54)
    t = "T O L D   I N   D A T A"
    w = d.textlength(t, font=k)
    d.text((ox + (W - w) / 2, 170), t, font=k, fill=ACCENT)
    # title
    t1 = F("ExtraBold", 236)
    for i, line in enumerate(["THE", "LAST", "PAYCHECK"]):
        w = d.textlength(line, font=t1)
        d.text((ox + (W - w) / 2, 330 + i * 258), line, font=t1, fill=INK)
    # rule
    d.rectangle([ox + W/2 - 90, 1180, ox + W/2 + 90, 1194], fill=ACCENT)
    # subtitle
    s = F("Regular", 76)
    for i, line in enumerate(["Which Jobs AI Is Really Taking —", "and Which Are Safe"]):
        w = d.textlength(line, font=s)
        d.text((ox + (W - w) / 2, 1270 + i * 104), line, font=s, fill=(205, 203, 199))
    # motif
    slope_motif(d, ox + W * 0.22, 1850, W * 0.56, 420, 10)
    # author
    a = F("SemiBold", 86)
    t = "AMIR M. KHAN"
    w = d.textlength(t, font=a)
    d.text((ox + (W - w) / 2, H - 260), t, font=a, fill=INK)

# ---------- ebook cover ----------
W, H = 1600, 2560
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
draw_front(d, W, H)
img.save("/home/claude/book/cover_ebook_1600x2560.jpg", quality=92)
print("ebook cover done")

# ---------- paperback wrap ----------
PAGES = 99
DPI = 300
spine_in = PAGES * 0.0025          # cream paper
bleed = 0.125
trim_w, trim_h = 6.0, 9.0
full_w = int(round((2 * (trim_w + bleed) + spine_in) * DPI))
full_h = int(round((trim_h + 2 * bleed) * DPI))
spine_px = int(round(spine_in * DPI))
panel_px = int(round((trim_w + bleed) * DPI))

wrap = Image.new("RGB", (full_w, full_h), BG)
d = ImageDraw.Draw(wrap)

# front panel (right side)
fx = panel_px + spine_px
# scale: draw front at panel size using same proportions (panel 1837x2775)
front = Image.new("RGB", (panel_px, full_h), BG)
fd = ImageDraw.Draw(front)
# reuse draw_front scaled: render big then resize
big = Image.new("RGB", (1600, 2560), BG)
bd = ImageDraw.Draw(big)
draw_front(bd, 1600, 2560)
front_scaled = big.resize((panel_px, full_h), Image.LANCZOS)
wrap.paste(front_scaled, (fx, 0))

# spine
if spine_px >= 60:  # KDP allows spine text if pages >= 79
    spine = Image.new("RGB", (full_h, spine_px), BG)
    sd = ImageDraw.Draw(spine)
    st = F("SemiBold", min(44, spine_px - 24))
    sd.text((int(full_h*0.10), (spine_px - st.size) // 2 - 4), "THE LAST PAYCHECK", font=st, fill=INK)
    at = F("Regular", min(38, spine_px - 28))
    w = sd.textlength("AMIR M. KHAN", font=at)
    sd.text((full_h - int(full_h*0.085) - w, (spine_px - at.size) // 2 - 2), "AMIR M. KHAN", font=at, fill=GREY)
    spine = spine.rotate(-90, expand=True)
    wrap.paste(spine, (panel_px, 0))

# back panel
margin = int(0.75 * DPI)
x0 = margin
maxw = panel_px - int(1.3 * DPI)

def wrap_text(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    lines.append(cur); return lines

y = int(0.85 * DPI)
h1 = F("Bold", 64)
d.text((x0, y), "The robots did not come for “jobs.”", font=h1, fill=ACCENT); y += 78
d.text((x0, y), "They came for tasks — and the data finally shows whose.", font=F("Bold", 48), fill=INK)
y += 110

blurb = ("Between 2023 and 2026, the first real measurements of AI and work arrived: "
         "payroll records covering millions of workers, job postings by the billion, "
         "the AI companies' own usage logs, and randomized workplace experiments. "
         "The Last Paycheck assembles them into one honest picture — which occupations are "
         "actually shrinking, which are quietly booming, why the youngest workers are hit first, "
         "and a 30-minute method to score your own job before your employer does. "
         "No hype, no doom: every number carries an endnote, and every chart can be rebuilt "
         "from public data.")
body = F("Regular", 42)
for line in wrap_text(d, blurb, body, maxw):
    d.text((x0, y), line, font=body, fill=(210, 208, 204)); y += 58
y += 50

stats = [
 "19%  — how far young workers in AI-exposed jobs sit below trend",
 "34%  — the productivity jump for novices working with AI",
 "1 in 4  — jobs worldwide exposed to generative AI",
]
sf = F("SemiBold", 44)
for s_ in stats:
    d.rectangle([x0, y + 8, x0 + 16, y + 52], fill=ACCENT)
    d.text((x0 + 44, y), s_, font=sf, fill=INK); y += 86
y += 60

bio = ("Amir Khan is a data analyst and independent researcher with nine years in "
       "executive support, analytics, and research administration — a career built of "
       "exactly the tasks this book measures.")
for line in wrap_text(d, bio, F("Regular", 38), maxw):
    d.text((x0, y), line, font=F("Regular", 38), fill=GREY); y += 52

# barcode white box (bottom-right of back panel): 2" x 1.2"
bw, bh = int(2.0 * DPI), int(1.2 * DPI)
bx = panel_px - bw - int(0.375 * DPI)
by = full_h - bh - int(0.375 * DPI)
d.rectangle([bx, by, bx + bw, by + bh], fill=(255, 255, 255))

wrap.save("/home/claude/book/cover_paperback_wrap_6x9_99p.pdf", "PDF", resolution=300)
wrap.save("/home/claude/book/cover_paperback_wrap_preview.jpg", quality=85)
print("wrap done", full_w, "x", full_h, "spine", spine_in, "in")
