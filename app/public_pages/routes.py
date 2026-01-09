from flask import Blueprint

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return "Hello World"

@public_bp.route("/article/<article_id>")
def article(article_id: int):
    return f"Article {article_id}"