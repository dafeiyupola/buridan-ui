import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.utils.routes import (
    BASE_UI_COMPONENTS,
    CHARTS_URLS,
    GET_STARTED_URLS,
    RESOURCES_URLS,
    UTILITIES,
)

BASE_URL = "https://buridan.reflex.run"

TOP_LEVEL = ["/", "/components", "/charts", "/create"]


def generate_sitemap() -> str:
    all_routes = (
        GET_STARTED_URLS + RESOURCES_URLS + BASE_UI_COMPONENTS + CHARTS_URLS + UTILITIES
    )

    top = "\n".join(f"  <url><loc>{BASE_URL}{path}</loc></url>" for path in TOP_LEVEL)

    pages = "\n".join(
        f"  <url><loc>{BASE_URL}/{route['url']}</loc></url>"
        for route in all_routes
        if route.get("url") and route["url"] != "llms.txt"
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{top}
{pages}
</urlset>"""


if __name__ == "__main__":
    output_path = Path(__file__).parent.parent / "assets" / "sitemap.xml"
    sitemap = generate_sitemap()
    output_path.write_text(sitemap, encoding="utf-8")
    print(f"sitemap.xml written to {output_path}")
