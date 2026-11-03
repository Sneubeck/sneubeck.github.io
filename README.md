# Shelby Lee Neubeck — one-page portfolio

Python + Pelican + Jinja2 static site with a mid-century-inspired custom design. The homepage has anchor sections for About, Resume, Writing, and Contact. Blog content remains a future capability but is not rendered or linked until activated intentionally.

## Preview locally

```bash
git switch portfolio/pelican-first-draft
git pull
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pelican content -s pelicanconf.py
python3 -m http.server 8000 -d output
```

Visit http://localhost:8000. If you already have the environment, skip creating it and installing requirements. Stop with Ctrl+C.

## Updating content

- Edit the one-page template in `theme/templates/index.html`.
- Edit styles in `theme/static/css/main.css`.
- Edit linked writing samples in `data/writing.json`.
- Replace photo placeholders with images you approve; currently no personal images are included.
- Resume and biography are from the provided documents/text, with the full supplied resume bullets and skill categories.

## Email privacy

The site does not print a literal email address into the generated HTML. Visitors can reveal a link with a click; the address is assembled by JavaScript from character codes on demand. This reduces simple scraping, but **cannot eliminate spam**: automated browsers may execute JavaScript, and any public email address can be copied. For stronger protection, use a privacy-preserving contact form or LinkedIn messages only. A previous commit on this public branch included a literal email in source, so changing the current HTML does not erase it from Git history.

## Publishing

This is a draft PR. GitHub Pages publishing is not configured. No automatic deployment is performed.

## Future blog

Pelican and blog templates remain in source for later. When you are ready, enable an article path, archive and feed settings in `pelicanconf.py`, then add Markdown posts to `content/`.
