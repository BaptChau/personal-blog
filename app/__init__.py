from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ma-cle-secrete"
    from app.public_pages.routes import public_bp
    from app.admin.routes import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.config["ADMIN_USER"] = 'admin'
    app.config["ADMIN_PASS"] = 'admin'
    return app