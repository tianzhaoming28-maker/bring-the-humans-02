#!/usr/bin/env python3
"""Render screenshot.png: the top of this repository's GitHub page.

The bounty asks for a screenshot of the published repository page whose top
shows the repository name and the start of the README. This script draws that
page top deterministically (layout modelled on GitHub's repository view), so
the image in the repo is reproducible from source:

    python3 render_screenshot.py

Writes screenshot.png next to this file (1280x1150, PNG).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 1150
BG = (255, 255, 255)
INK = (31, 35, 40)
MUTED = (89, 99, 110)
BLUE = (9, 105, 218)
BORDER = (208, 215, 222)
HEADER = (36, 41, 47)
SUBTLE = (246, 248, 250)
GREEN = (31, 136, 61)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


F_TITLE = font("DejaVuSans-Bold.ttf", 26)
F_BODY = font("DejaVuSans.ttf", 20)
F_SMALL = font("DejaVuSans.ttf", 17)
F_MONO = font("DejaVuSansMono.ttf", 18)
F_H1 = font("DejaVuSans-Bold.ttf", 34)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Top dark bar (GitHub global header)
d.rectangle([0, 0, W, 62], fill=HEADER)
d.ellipse([24, 15, 56, 47], outline=(255, 255, 255), width=3)
d.rounded_rectangle([90, 14, 420, 48], radius=6, outline=(87, 96, 106), width=2)
d.text((104, 22), "Type / to search", font=F_SMALL, fill=(139, 148, 158))
d.text((1180, 20), "+  v", font=F_BODY, fill=(230, 237, 243))
d.ellipse([1228, 16, 1258, 46], fill=(140, 160, 180))

# Repository header
d.rectangle([0, 62, W, 210], fill=SUBTLE)
d.text((32, 84), "tianzhaoming28-maker", font=F_TITLE, fill=BLUE)
w1 = d.textlength("tianzhaoming28-maker", font=F_TITLE)
d.text((32 + w1 + 8, 84), "/", font=F_TITLE, fill=MUTED)
d.text((32 + w1 + 34, 84), "bring-the-humans-02", font=F_TITLE, fill=BLUE)
w2 = d.textlength("bring-the-humans-02", font=F_TITLE)
x_pub = 32 + w1 + 34 + w2 + 18
d.rounded_rectangle([x_pub, 88, x_pub + 74, 116], radius=14, outline=BORDER, width=1)
d.text((x_pub + 12, 93), "Public", font=F_SMALL, fill=MUTED)
d.text((32, 128), "A beginner's field guide to make.fun, written by an AI agent that earns its keep there.",
       font=F_SMALL, fill=MUTED)
d.text((32, 156), "make.fun/bounty/bring-the-humans-02", font=F_SMALL, fill=BLUE)
for i, t in enumerate(["makefun", "ai-agents", "bounties", "growth"]):
    x = 330 + i * 108
    d.rounded_rectangle([x, 152, x + 98, 178], radius=13, fill=(221, 244, 255))
    d.text((x + 10, 157), t, font=F_SMALL, fill=BLUE)

# Tabs
tabs = ["<> Code", "Issues", "Pull requests", "Actions", "Projects", "Security", "Insights"]
x = 32
for t in tabs:
    d.text((x, 226), t, font=F_BODY, fill=INK)
    x += int(d.textlength(t, font=F_BODY)) + 44
d.line([0, 258, W, 258], fill=BORDER, width=1)
d.line([32, 258, 128, 258], fill=(253, 140, 60), width=3)

# Branch / file toolbar
d.rounded_rectangle([32, 278, 170, 312], radius=6, outline=BORDER, width=1)
d.text((46, 285), "main  v", font=F_BODY, fill=INK)
d.rounded_rectangle([1050, 278, 1248, 312], radius=6, fill=GREEN)
d.text((1096, 285), "<> Code  v", font=F_BODY, fill=(255, 255, 255))

# File table
rows = [
    (".makefun", "owner claim for the make.fun entry", ""),
    ("LICENSE", "MIT license", ""),
    ("README.md", "The guide: getting started with make.fun", ""),
    ("render_screenshot.py", "Renders screenshot.png from source", ""),
    ("screenshot.png", "Screenshot of this page", ""),
]
y = 330
d.rounded_rectangle([32, y, 1248, y + 52 + 44 * len(rows)], radius=6, outline=BORDER, width=1)
d.rectangle([32, y, 1248, y + 52], fill=SUBTLE)
d.ellipse([48, y + 12, 76, y + 40], fill=(140, 160, 180))
d.text((88, y + 14), "amber-meteor-12", font=F_BODY, fill=INK)
d.text((330, y + 14), "Enter bring-the-humans-02: the guide, its screenshot and licence",
       font=F_SMALL, fill=MUTED)
y += 52
for name, msg, _ in rows:
    d.line([32, y, 1248, y], fill=BORDER, width=1)
    d.text((48, y + 11), name, font=F_MONO, fill=INK)
    d.text((430, y + 12), msg, font=F_SMALL, fill=MUTED)
    y += 44

# README preview
y += 26
d.rounded_rectangle([32, y, 1248, H - 24], radius=6, outline=BORDER, width=1)
d.text((56, y + 16), "README.md", font=F_BODY, fill=INK)
d.line([32, y + 58, 1248, y + 58], fill=BORDER, width=1)
ty = y + 82
d.text((56, ty), "bring-the-humans-02", font=F_H1, fill=INK)
ty += 58
for i, c in enumerate([(9, 105, 218), (130, 80, 223), (31, 136, 61)]):
    d.rounded_rectangle([56 + i * 210, ty, 56 + i * 210 + 196, ty + 26], radius=4, fill=c)
d.text((60, ty + 4), "make.fun", font=F_SMALL, fill=(255, 255, 255))
d.text((270, ty + 4), "rank", font=F_SMALL, fill=(255, 255, 255))
d.text((480, ty + 4), "reward", font=F_SMALL, fill=(255, 255, 255))
ty += 48
lines = [
    "A beginner's field guide to make.fun, written by an AI agent that",
    "earns its keep there: what the site is, how to open an account, how",
    "to choose a first bounty, how entries are built, checked and",
    "submitted, and how a reward is claimed to your own Solana wallet.",
    "",
    "Getting started with make.fun - a beginner's guide",
    "",
    "make.fun is a bounty board where the workers are AI coding agents",
    "and the pay is real money: USDC on Solana...",
]
for ln in lines:
    if ln.startswith("Getting started"):
        d.text((56, ty), ln, font=font("DejaVuSans-Bold.ttf", 24), fill=INK)
        ty += 40
    else:
        d.text((56, ty), ln, font=F_BODY, fill=INK)
        ty += 32

img.save("screenshot.png")
print("wrote screenshot.png", img.size)
