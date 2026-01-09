from flask import Blueprint, render_template

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return render_template("home.html")

@public_bp.route("/article/<article_id>")
def article(article_id: int):
    return render_template("article.html", article_id=article_id)