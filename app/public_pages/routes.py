from flask import Blueprint, render_template
from app.admin import helper
public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    articles = helper.get_all_articles()
    return render_template("home.html", articles=articles)

@public_bp.route("/article/<article_id>")
def article(article_id: int):
    article = helper.get_article_by_id(article_id)
    return render_template("article.html", article=article)