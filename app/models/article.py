from dataclasses import dataclass
from datetime import date

from flask import Request


@dataclass
class Article:
    id: int
    title: str
    content: str
    publishing_date: date

    _next_id = 1

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "publishing_date": self.publishing_date.isoformat()
        }

    @classmethod
    def from_request(cls, request: Request) -> Article:
        article = Article(
            id= cls._next_id,
            title=request.form.get("title", "").strip(),
            content=request.form.get("content", "").strip(),
            publishing_date=date.today()
        )

        cls._next_id += 1
        return article