from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def home():
    return "Admin Page"

@admin_bp.route("/articles/add")
def add_article():
    return "Add article"

@admin_bp.route("/articles/<article_id>/edit")
def edit_article(article_id: int):
    return f"Edit article{article_id}"