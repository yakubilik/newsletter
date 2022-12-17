from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def about():
    return render_template("about.html")


@views.route("/home")
def home():
    my_data = [{"title":"1","icerik":"Lorem ipsum 1","image":"/static/images/img_1.jpg"},
               {"title":"2","icerik":"Lorem ipsum 2","image":"/static/images/img_2.jpg"},
               {"title":"3","icerik":"Lorem ipsum 3","image":"/static/images/img_3.jpg"},
               {"title":"4","icerik":"Lorem ipsum 4","image":"/static/images/img_4.jpg"},
               {"title":"5","icerik":"Lorem ipsum 5","image":"/static/images/img_5.jpg"}]
    my_data2 = [1,2,3,4,5]
    return render_template("index.html", data=my_data)