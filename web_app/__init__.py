from flask import Flask
from .models import DB_NAME
import os



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'pVXnfPj$B)IqY$28'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql:///{DB_NAME}"
    app.app_context()


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    from .models import Admin, News
    from .models import create_database
    session = create_database()


    return app


