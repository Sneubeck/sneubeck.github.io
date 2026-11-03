# Shelby Lee Neubeck — portfolio

A Python-powered portfolio and future blog, built with [Pelican](https://getpelican.com/) and a custom Jinja2 theme.

## Preview locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pelican content -s pelicanconf.py
python -m http.server 8000 -d output
```

Open http://localhost:8000.

## Add a blog post

Create `content/your-post.md`:

```markdown
Title: Your post title
Date: 2026-11-03 12:00
Category: Notes
Slug: your-post-title

Write your post in Markdown here.
```

Run `pelican content -s pelicanconf.py` to rebuild. Blog posts will appear under `/blog/`, with an Atom feed at `/feeds/all.atom.xml`.

## Edit writing samples

Update `data/writing.json`. Each entry has `title`, `category`, `publication`, and `url`. The homepage and writing archive use the same data.

## Publish later (not enabled yet)

This branch intentionally does **not** configure GitHub Pages or automatic deployment. After reviewing and merging, configure GitHub Pages with a GitHub Actions deployment workflow. Until then, this is a source-code preview only.

All copy and links should be reviewed before publication. The writing archive is curated from the provided Google Doc; additional samples can be added at any time.
