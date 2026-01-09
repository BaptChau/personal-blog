from pathlib import Path
import json

from app.models.article import Article


def save_article_to_file(article: Article):
    storage_dir = Path("app/storage")
    file_path = storage_dir / f"{article.id}.json"

    data = article.to_dict()
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        return False
    return True