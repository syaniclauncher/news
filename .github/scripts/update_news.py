import json
import requests

mojang_launchercontent_url = "https://launchercontent.mojang.com"
news_api = mojang_launchercontent_url + "/v2/news.json"

response = requests.get(news_api, timeout=10)
response.raise_for_status()
feed = response.json()

news = [
    {
        "title": entry.get("title", ""),
        "text": entry.get("text", ""),
        "date": entry.get("date", ""),
        "tag": entry.get("tag") or entry.get("category", ""),
        "url": entry.get("readMoreLink", ""),
        "image": (
            entry.get("newsPageImage", {}).get("url", "")
            if entry.get("newsPageImage")
            else ""
        ),
    }
    for entry in feed.get("entries", [])
    if entry.get("category") == "Minecraft: Java Edition"
]

for item in news:
    if item["image"] and not item["image"].startswith(("http://", "https://")):
        item["image"] = mojang_launchercontent_url + (
            "" if item["image"].startswith("/") else "/"
        ) + item["image"]

with open("minecraft_news.json", "w", encoding="utf-8") as f:
    json.dump(news[:6], f, indent=2, ensure_ascii=False)
