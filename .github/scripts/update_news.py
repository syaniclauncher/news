import json
import requests

url = "https://launchercontent.mojang.com/v2/news.json"

feed = requests.get(url, timeout=10).json()

news = [
    {
        "title": entry.get("title", ""),
        "text": entry.get("text", ""),
        "date": entry.get("date", ""),
        "tag": entry.get("tag") or entry.get("category", ""),
        "url": entry.get("readMoreLink", ""),
        "image": (entry.get("newsPageImage") or {}).get("url", ""),
    }
    for entry in feed.get("entries", [])
    if entry.get("category") == "Minecraft: Java Edition"
]

with open("minecraft_news.json", "w", encoding="utf-8") as f:
    json.dump(news[:6], f, indent=2, ensure_ascii=False)
