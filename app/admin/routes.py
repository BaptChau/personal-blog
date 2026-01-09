from flask import Blueprint, render_template

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def home():
    return render_template('admin/dashboard')

@admin_bp.route("/article/add")
def add_article():
    return render_template('admin/add_article.html')

@admin_bp.route("/article/<article_id>/edit")
def edit_article(article_id: int):
    return render_template('admin/edit_article.html', article_id=article_id)