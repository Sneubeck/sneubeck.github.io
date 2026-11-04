# Shelby Lee Neubeck — Portfolio

A single-page personal portfolio built with [Pelican](https://getpelican.com/) and a custom responsive theme. It includes an introduction, professional experience, skills, education, published writing, and contact links.

## Technology

- **Static site generation:** Python, Pelican 4.x, and Jinja2
- **Frontend:** Semantic HTML, CSS, and vanilla JavaScript
- **Typography:** Fraunces and DM Sans
- **Assets:** SVG illustrations and WebP photography
- **Content:** JSON-based writing archive rendered through Jinja2

## Implementation

The site uses a custom Pelican theme with a single generated homepage. The responsive layout is defined in CSS, without a frontend framework or JavaScript build pipeline.

JavaScript handles category filtering for the writing archive, section-aware navigation, and the on-demand email contact link. Internal assets use relative URLs, and the resume is available as a downloadable A4 PDF.

## Project structure

```text
content/                    Pelican content directory
data/writing.json           Published writing entries
theme/
  templates/
    base.html               Shared page layout and navigation
    index.html              Portfolio homepage
  static/
    css/main.css            Responsive design and styles
    img/                    Photographs and SVG illustrations
    resume/                 Downloadable resume PDF
pelicanconf.py              Pelican configuration
requirements.txt            Python dependencies
```

## Build

```bash
pip install -r requirements.txt
pelican content -s pelicanconf.py
```

The generated static site is written to `output/`.
