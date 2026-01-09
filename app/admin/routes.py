from flask import Blueprint, render_template, request, redirect
from app.models.article import Article
from app.admin.helper import save_article_to_file

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def home():
    return render_template('admin/dashboard.html')

@admin_bp.route("/article/add", methods=["GET"])
def add_article():
    return render_template('admin/add_article.html')

@admin_bp.route("/article/save", methods=["POST"])
def save_article():
    article = Article.from_request(request)

    result = save_article_to_file(article)

    if result:
        return redirect('/admin/')
    return redirect('/admin/article/add')
@admin_bp.route("/article/<article_id>/edit")
def edit_article(article_id: int):
    return render_template('admin/edit_article.html', article_id=article_id)