from flask import Blueprint, render_template,request, redirect, url_for
from .models import News, create_database
from .side_functions import fresh_news
from flask_login import login_required,  current_user
from sqlalchemy import func
views = Blueprint('views', __name__)



@views.route("/detail",methods = ["GET","POST"])
def about():
    session = create_database()
    if request.method == "POST":
        img_id = request.form.get("read_more")
        item = session.query(News).get(img_id)
    else:
        item = session.query(News).get(1)
    return render_template("about.html", data=item)


@views.route("/home", methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == "FRESH!":
            fresh_news()

    session = create_database()
    #my_data = session.query(News).order_by(func.random()).offset(20).limit(100).all()
    my_data = session.query(News).all()
    return render_template("index.html", data=my_data)
@views.route("/add_news",methods=["GET","POST"])
@login_required
def add_news():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        image = request.form["image"]
        session = create_database()
        news = session.query(News).all()
        if len(news) > 1:
            id = News.session.query(func.max(News.id)).scalar() + 1
        else:
            id = 1

        new = News(id=id,title=title, content=content,image=image)
        session.add(new)
        session.commit()
        return redirect(url_for("views.home"))
    return render_template("add_news.html")


