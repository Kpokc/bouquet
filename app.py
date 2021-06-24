import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
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
    posts = mongo.db.post.find()
    return render_template("cards.html", posts=posts)


@app.route("/read_post/<post_id>")
def read_post(post_id):
    """
        Single post on a new page
    """
    post = mongo.db.post.find_one(
        {"_id": ObjectId(post_id)}
    )
    return render_template("read_post.html", post=post)
    # #, methods=["GET","POST"]


today = date.today()
now = datetime.now()
@app.route("/add_post", methods=["GET","POST"])
def add_post():
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
        #flash("Task Successfully Added")
        return redirect(url_for("welcome"))

    categories = mongo.db.categories.find()
    return render_template("add_post.html", categories=categories)


@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)