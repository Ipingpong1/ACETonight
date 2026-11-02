#!/usr/bin/env python3
"""Render preprint.md and supplement.md to HTML and PDF.

usage: python build.py            (from any directory)
Requires: the `markdown` package and Google Chrome (headless) or Chromium.
"""
import pathlib, re, shutil, subprocess, sys, tempfile

try:
    import markdown
except ImportError:
    sys.exit("pip install markdown")

HERE = pathlib.Path(__file__).resolve().parent
DOCS = ["preprint", "supplement"]

CSS = """
@page { size: A4; margin: 18mm 17mm; }
html { font-size: 10.5pt; }
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.42; color: #111; max-width: 180mm; margin: 0 auto; padding: 0 4mm; }
h1 { font-size: 1.55em; line-height: 1.25; margin: 0 0 .4em; }
h2 { font-size: 1.25em; margin: 1.6em 0 .5em; border-bottom: 1px solid #bbb; padding-bottom: .15em; }
h3 { font-size: 1.05em; margin: 1.3em 0 .4em; }
p { margin: .45em 0 .7em; text-align: justify; }
li { margin: .2em 0; }
.box { border: 1px solid #8a8a8a; background: #f4f4f2; padding: .6em 1em; margin: 1em 0; page-break-inside: avoid; }
.box p { text-align: left; }
table { border-collapse: collapse; font-size: .8em; margin: .8em 0 1em; width: 100%; page-break-inside: auto; }
th, td { border-top: 1px solid #ccc; border-bottom: 1px solid #ccc; padding: .25em .45em; vertical-align: top; }
th { background: #eee; text-align: left; }
tr { page-break-inside: avoid; }
img { max-width: 100%; display: block; margin: 1em auto .4em; page-break-inside: avoid; }
img + p { font-size: .9em; }
sup { font-size: .7em; }
code { font-family: Menlo, Consolas, monospace; font-size: .85em; }
blockquote { margin: .6em 1.2em; color: #333; }
ol li { margin: .3em 0; }
em.note { color: #555; }
p.eq { text-align: center; margin: .8em 0; font-size: 1.02em; }
a { color: #1a4a8a; text-decoration: none; }
"""


def render(name):
    src = HERE / f"{name}.md"
    text = src.read_text(encoding="utf-8")
    # protect $$...$$ display math from markdown's emphasis parsing
    blocks = []
    def keep(m):
        blocks.append(m.group(0)); return f"@@MATH{len(blocks)-1}@@"
    text = re.sub(r"\$\$.*?\$\$", keep, text, flags=re.S)
    html = markdown.markdown(text, extensions=["tables", "footnotes", "attr_list", "md_in_html", "sane_lists", "smarty"],
                             extension_configs={"smarty": {"smart_quotes": False}})
    for i, b in enumerate(blocks):
        html = html.replace(f"@@MATH{i}@@", b)
    title = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    title = re.sub(r"<[^>]+>", "", title.group(1)) if title else name
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>'
           f'<style>{CSS}</style></head>'
           f'<body><main>{html}</main></body></html>')
    out = HERE / f"{name}.html"
    out.write_text(doc, encoding="utf-8")
    return out


def to_pdf(html_path):
    chrome = next((c for c in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser") if shutil.which(c)), None)
    if not chrome:
        print("no Chrome/Chromium found; HTML only"); return None
    pdf = html_path.with_suffix(".pdf")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox", f"--user-data-dir={tmp}", "--no-pdf-header-footer",
               "--run-all-compositor-stages-before-draw", "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", html_path.as_uri()]
        subprocess.run(cmd, check=True, timeout=300, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return pdf


if __name__ == "__main__":
    for n in DOCS:
        h = render(n); p = to_pdf(h)
        print(n, "->", h.name, "and", p.name if p else "(no pdf)")
