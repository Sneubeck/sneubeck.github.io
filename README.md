# Shelby Lee Neubeck — one-page portfolio

Python + Pelican + Jinja2 static site with a mid-century-inspired custom design. The homepage has anchor sections for About, Resume, Writing, and Contact. The site is intentionally a single-page portfolio; no unused blog templates or illustrations are shipped.

## Preview locally

```bash
git switch portfolio/leaf-and-content-refresh
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
- Hero photos are `theme/static/img/shelby-hero-primary.webp` and `theme/static/img/shelby-hero-secondary.webp`. Both are committed and used by the homepage.
- Resume and biography are from the provided documents/text, with the full supplied resume bullets and skill categories.

## Email privacy

The site does not print a literal email address into the generated HTML. Visitors can reveal a link with a click; the address is assembled by JavaScript from character codes on demand. This reduces simple scraping, but **cannot eliminate spam**: automated browsers may execute JavaScript, and any public email address can be copied. For stronger protection, use a privacy-preserving contact form or LinkedIn messages only. A previous commit on this public branch included a literal email in source, so changing the current HTML does not erase it from Git history.

## Publishing

The portfolio is being developed on a feature branch and reviewed through a pull request. Confirm GitHub Pages configuration separately before publishing.

## Site assets and URLs

Internal image and stylesheet URLs are relative to the generated homepage. Hero portraits live at `theme/static/img/shelby-hero-primary.webp` and `theme/static/img/shelby-hero-secondary.webp`. External writing sample, GitHub, and LinkedIn links remain absolute because they point off-site.

The CSS is organized by page section and responsive breakpoints. Only assets referenced by the current homepage remain. If a blog is added later, introduce its templates and styles then.
