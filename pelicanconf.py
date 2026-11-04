from pathlib import Path
import json

AUTHOR = "Shelby Lee Neubeck"
SITENAME = "Shelby Lee Neubeck"
SITEURL = ""
PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "en"
THEME = "theme"
DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = False
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

DIRECT_TEMPLATES = ["index"]
INDEX_SAVE_AS = "index.html"
ARTICLE_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = []
PORTFOLIO = json.loads((Path(__file__).parent / "data" / "writing.json").read_text(encoding="utf-8"))
