from flask import Blueprint,request, flash, redirect,url_for,render_template
from .models import Admin,create_database
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

def validate_login(email,password):
    session = create_database()
    item = session.query(Admin).filter(Admin.email==email).first()
    if item:
        if item.password == password:
            return item
        else:
           return False



@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        referer = request.referrer
        referer = referer.split("/")[3]
        if referer == auth:
            referer

        # Validate the login credentials
        user = validate_login(username, password)
        if not user:
            flash("Incorrect password!",category="error")
        else:
            # Login successful, redirect to the dashboard
            flash("Logged in successfully", category='success')
            login_user(user, remember=True)
            return redirect(url_for("views.add_news"))
    return render_template('login.html')


@auth.route("/logout")
def logout():
    logout_user()
