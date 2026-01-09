import shutil
from pathlib import Path
import json

from app.models.article import Article


def save_article_to_file(article: Article):
    storage_dir = Path("app/storage")
    file_path = storage_dir / f"article-{article.id}.json"

    data = article.to_dict()
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        return False
    return True

def get_all_articles():
    storage_dir = Path("app/storage")
    articles = []
    for file in storage_dir.glob("*.json"):
        with open(file, "r") as f:
            data = json.load(f)
            articles.append(Article(**data))
    return articles

def get_article_by_id(article_id: int) -> Article:
    storage_dir = Path("app/storage")
    file_path = storage_dir / f"article-{article_id}.json"
    with open(file_path, "r") as f:
        data = json.load(f)
        return Article.from_json(data)

def remove_article_from_file(article_id: int) -> None:
    storage_dir = Path("app/storage")
    archived_dir = storage_dir / "archived"
    file_path = storage_dir / f"article-{article_id}.json"
    target = archived_dir / file_path.name

    shutil.move(file_path, target)