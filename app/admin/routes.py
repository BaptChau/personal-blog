from flask import Blueprint, render_template, request, redirect
from app.models.article import Article
import app.admin.helper as helper
admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def home():
    articles = helper.get_all_articles()
    return render_template('admin/dashboard.html', articles=articles)

@admin_bp.route("/article/add", methods=["GET"])
def add_article():
    return render_template('admin/add_article.html')

@admin_bp.route("/article/save", methods=["POST"])
def save_article():
    article = Article.from_request(request)

    result = helper.save_article_to_file(article)

    if result:
        return redirect('/admin/')
    return redirect('/admin/article/add')

@admin_bp.route("/article/<article_id>/edit", methods=["POST"])
def update_article(article_id: int):
    article = helper.get_article_by_id(article_id)
    article.title = request.form["title"].strip()
    article.content = request.form["content"].strip()
    result = helper.save_article_to_file(article)

    if result:
        return redirect('/admin/')
    return redirect('/admin/article/add')


@admin_bp.route("/article/<article_id>/edit", methods=["GET"])
def edit_article(article_id: int):
    article = helper.get_article_by_id(article_id)
    return render_template('admin/edit_article.html', article=article)

@admin_bp.route("/article/<article_id>/delete")
def delete_article(article_id: int):
    helper.remove_article_from_file(article_id)
    return redirect('/admin/')