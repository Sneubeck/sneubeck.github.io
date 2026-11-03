from pathlib import Path
import json

AUTHOR = "Shelby Lee Neubeck"
SITENAME = "Shelby Lee Neubeck"
SITESUBTITLE = "Words, communities & the occasional bug."
SITEURL = ""
PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "en"
THEME = "theme"
DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = False
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
ARCHIVES_SAVE_AS = "blog/index.html"
DIRECT_TEMPLATES = ["index", "writing", "resume", "archives"]
WRITING_SAVE_AS = "writing.html"
RESUME_SAVE_AS = "resume.html"
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = []
PORTFOLIO = json.loads((Path(__file__).parent / "data" / "writing.json").read_text(encoding="utf-8"))
