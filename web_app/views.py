from flask import Blueprint, render_template,request
from .models import create_database
from .models import News
from .side_functions import fresh_news

views = Blueprint('views', __name__)

@views.route("/")
def about():
    return render_template("about.html")


@views.route("/home", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == "FRESH!":
            fresh_news()

    session = create_database()
    my_data = session.query(News).order_by(News.id.desc())
    return render_template("index.html", data=my_data)