import os
from flask import (
    Flask, flash, render_template,
    redirect)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/add_post")
def add_post():
    return render_template("add_post.html")


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