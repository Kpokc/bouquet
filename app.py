import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import date, datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/welcome")
def welcome():
    """
        index page
    """
    posts = mongo.db.post.find()
    return render_template("cards.html", posts=posts)


@app.route("/read_post/<post_id>")
def read_post(post_id):
    """
        Read single post on a new page
    """
    post = mongo.db.post.find_one(
        {"_id": ObjectId(post_id)}
    )
    return render_template("read_post.html", post=post)


@app.route("/add_post", methods=["GET","POST"])
def add_post():
    """
        Add post do DB
    """
    today = date.today()
    now = datetime.now()
    if request.method == "POST":
        post = {
            "user_id": "N/A",
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now,
            "img_src": request.form.get("img_src")
        }
        mongo.db.post.insert_one(post)
        flash("Post Successfully Added!")
        return redirect(url_for("welcome"))

    categories = mongo.db.categories.find()
    return render_template("add_post.html", categories=categories)


@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/login", methods=["GET","POST"])
def login():
    """
        Login function
    """
    if request.method == "POST":
        get_user = mongo.db.user.find_one(
            {"username": request.form.get("username")}
        )

    return render_template("login.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    """
        Signup function
    """
    if request.method == "POST":
        get_user = mongo.db.user.find_one(
            {"username": request.form.get("username")}
        )

        if get_user:
            flash("User already exists!")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username"),
            "password": request.form.get("password")
        }
        mongo.db.user.insert(signup)

        #Add user into cookie
        session["user"] = request.form.get("username")
        flash("We are glad that you joined us!")
        return redirect(url_for("welcome"))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)