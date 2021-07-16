import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


today = date.today()
now = datetime.now()


@app.route("/")
@app.route("/welcome")
def welcome():
    """
        index page
    """
    posts = list(mongo.db.post.find().sort("time", -1))

    for post in posts:
        # (nl to br) replace new line with page break
        post["content"] = post["content"].replace('\n', '<br />')
        # \t to tab (8 spaces)
        tab = "&nbsp;" * 8
        post["content"] = post["content"].replace('\t', tab)

    categories = list(mongo.db.categories.find())
    users = list(mongo.db.user.find())
    likes = list(mongo.db.likes.find())
    dislikes = list(mongo.db.dislikes.find())
<<<<<<< HEAD
    pined = list(mongo.db.pined.find())
    return render_template("cards.html", posts=posts, categories=categories, users=users, likes=likes, dislikes=dislikes, pined=pined)
=======
    pinned = list(mongo.db.pinned.find())
    return render_template("cards.html", posts=posts, categories=categories, users=users, likes=likes, dislikes=dislikes, pinned=pinned)
>>>>>>> f12759bd4f22ad7430891922052820550b97d50e


@app.route("/read_post/<post_id>")
def read_post(post_id):
    """
        Read single post on a new page
    """
    post = mongo.db.post.find_one(
        {"_id": ObjectId(post_id)}
    )

    # (nl to br) replace new line with page break
    post["content"] = post["content"].replace('\n', '<br />')
    # \t to tab (8 spaces)
    tab = "&nbsp;" * 8
    post["content"] = post["content"].replace('\t', tab)

    categories = list(mongo.db.categories.find())
    users = list(mongo.db.user.find())
    comments = list(mongo.db.comments.find())
    likes = list(mongo.db.likes.find())
    dislikes = list(mongo.db.dislikes.find())
    pinned = list(mongo.db.pinned.find())
    return render_template("read_post.html", post=post, categories=categories, users=users, comments=comments, likes=likes, dislikes=dislikes, pinned=pinned)


@app.route("/add_post", methods=["GET","POST"])
def add_post():
    """
        Add post do DB
    """
    if request.method == "POST":
        # Get user info by his sessions name 
        user_id = mongo.db.user.find_one(
            {"username": session["user"]}
        )
        post = {
            "user_id": str(user_id["_id"]), # add user id
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now,
            "img_src": request.form.get("img_src"),
        }
        mongo.db.post.insert_one(post)
        flash("Post Successfully Added!")
        return redirect(url_for("welcome"))

    categories = mongo.db.categories.find()
    return render_template("add_post.html", categories=categories)


@app.route("/edit_post/<post_id>", methods=["GET","POST"])
def edit_post(post_id):
    """
        Edit post
    """
    if request.method == "POST":
        # Get user info by his sessions name 
        user_id = mongo.db.user.find_one(
            {"username": session["user"]}
        )
        post = {
            "user_id": str(user_id["_id"]), # add user id
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now,
            "img_src": request.form.get("img_src")
        }
        mongo.db.post.update({"_id": ObjectId(post_id)}, post)
        flash("Post was Updated!")

        return redirect(url_for("welcome"))

    post = mongo.db.post.find_one(
        {"_id": ObjectId(post_id)}
    )
    categories = mongo.db.categories.find()

    return render_template("edit_post.html", post=post, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    """
        Delete post
    """
    # Delete post
    mongo.db.post.remove({
        "_id":ObjectId(post_id)
    })
    # Deleted likes posts
    mongo.db.likes.remove({
        "post_id": str(ObjectId(post_id))
    })
    # Deleted dislikes posts
    mongo.db.dislikes.remove({
        "post_id": str(ObjectId(post_id))
    })
    # Delete related comments
    mongo.db.comments.remove({
        "post_id": str(ObjectId(post_id))
    })
    # Delete related complaint
    mongo.db.complaint.remove({
        "post_id": str(ObjectId(post_id))
    })
    flash("Post was Deleted!")
    return redirect(url_for("welcome"))


@app.route("/like/<post_id>", methods=["GET","POST"])
def like(post_id):
    """
        Like post
    """
<<<<<<< HEAD
    # Get user info by his sessions name 
    # user_id = mongo.db.user.find_one(
    #     {"username": session["user"]}
    # )
    like = ({
        "user_id": session["user"],
        "post_id": post_id
    })
    mongo.db.likes.insert_one(like)
=======
    dislikes = list(mongo.db.dislikes.find())
    likes = list(mongo.db.likes.find())

    # Check if user had disliked this post before if so delete
    if len(dislikes) > 0:
        for dislike in dislikes:
            if dislike["username"] == session["user"] and dislike["post_id"] == post_id:
                mongo.db.dislikes.delete_one({
                    "_id": ObjectId(dislike["_id"])
                })
    
    # Check if there is data in the likes table. 
    if len(likes) > 0:
        for like in likes:
            # Check if this post has been liked by current user.
            if like["username"] == session["user"] and like["post_id"] == post_id:
                # Notify user that this post was already liked
                flash("Only one like per post!")
                return redirect(url_for("welcome"))
            else:
                # Add to likes if not in the table
                like = ({
                    "username": session["user"],
                    "post_id": post_id
                })
                mongo.db.likes.insert_one(like)
    else:
        # Add to likes if table is empty.
        like = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.likes.insert_one(like)
>>>>>>> f12759bd4f22ad7430891922052820550b97d50e

    # return nothing
    return ('', 204)


def check_like(post_id):
    likes = list(mongo.db.likes.find())

    return post_id



@app.route("/dislike/<post_id>", methods=["GET","POST"])
def dislike(post_id):
    """
        Dislike post
    """
<<<<<<< HEAD
    # Get user info by his sessions name 
    # user_id = mongo.db.user.find_one(
    #     {"username": session["user"]}
    # )
    dislike = ({
        "user_id": session["user"],
        "post_id": post_id
    })
    mongo.db.dislikes.insert_one(dislike)
=======
    dislikes = list(mongo.db.dislikes.find())
    likes = list(mongo.db.likes.find())

    # Check if user had liked this post before if so delete
    if len(likes) > 0:
        for like in likes:
            if like["username"] == session["user"] and like["post_id"] == post_id:
                mongo.db.likes.delete_one({
                    "_id": ObjectId(like["_id"])
                })

    # Check if there is data in the dislikes table. 
    if len(dislikes) > 0:
        for dislike in dislikes:
            # Check if this post has been disliked by current user.
            if dislike["username"] == session["user"] and dislike["post_id"] == post_id:
                # Notify user that this post was already disliked
                flash("Only one dislike per post!")
                return redirect(url_for("welcome"))
            else:
                # Add to dislikes if not in the table
                dislike = ({
                    "username": session["user"],
                    "post_id": post_id
                })
                mongo.db.dislikes.insert_one(dislike)
    else:
        # Add to dislikes if table is empty.
        dislike = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.dislikes.insert_one(dislike)
>>>>>>> f12759bd4f22ad7430891922052820550b97d50e

    # return nothing
    return ('', 204)


@app.route("/pinned/<post_id>", methods=["GET","POST"])
def pinned(post_id):
    """
        Pin post to read later
    """
<<<<<<< HEAD
    # Get user info by his sessions name 
    # user_id = mongo.db.user.find_one(
    #     {"username": session["user"]}
    # )
    pin = ({
        "user_id": session["user"],
        "post_id": post_id
    })
    mongo.db.pined.insert_one(pin)
=======
    pinned = list(mongo.db.pinned.find())
    # Check if there is data in the pined table. 
    if len(pinned) > 0:
        for pin in pinned:
            # Check if this post has been pined by current user.
            if pin["username"] == session["user"] and pin["post_id"] == post_id:
                # Delete from pinned.
                mongo.db.pinned.delete_one({
                    "_id": ObjectId(pin["_id"])
                })
            else:
                # Add to pinned if not in the table.
                pin = ({
                    "username": session["user"],
                    "post_id": post_id
                })
                mongo.db.pinned.insert_one(pin)
    else:
        # Add to pinned if table is empty.
        pin = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.pinned.insert_one(pin)
>>>>>>> f12759bd4f22ad7430891922052820550b97d50e

    # return nothing
    return ('', 204)


@app.route("/comment/<post_id>", methods=["GET","POST"])
def comment(post_id):
    """
        Add comment
    """
    if request.method == "POST":
        # Get user info by his sessions name 
        user_id = mongo.db.user.find_one(
            {"username": session["user"]}
        )
        comment = ({
            "user_id": str(user_id["_id"]),
            "post_id": post_id,
            "comment": request.form.get("comment"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now
        })
        mongo.db.comments.insert_one(comment)

        return redirect(url_for("read_post", post_id=post_id))


@app.route("/edit_comment/<comment_id>", methods=["GET","POST"])
def edit_comment(comment_id):
    """
        Edit comment
    """
    if request.method == "POST":
        # Get user info by his sessions name 
        user_id = mongo.db.user.find_one(
            {"username": session["user"]}
        )
        old_comment = mongo.db.comments.find_one(
            {"_id": ObjectId(comment_id) }
        )
        comment = ({
            "user_id": str(user_id["_id"]),
            "post_id": old_comment["post_id"],
            "comment": request.form.get("comment"),
            "date" : old_comment["date"],
            "time": old_comment["time"]
        })
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, comment)

    post_id = mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)}
    )

    return redirect(url_for("read_post", post_id=post_id["post_id"]))


@app.route("/delete_comment/<comment_id>", methods=["GET","POST"])
def delete_comment(comment_id):
    """
        Delete comment
    """
    print(comment_id)
    comment = mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)}
    )

    print(comment["post_id"])
    #Delete post
    mongo.db.comments.remove({
        "_id":ObjectId(comment_id)
    })
    
    return redirect(url_for("read_post", post_id=comment["post_id"]))


@app.route("/mypage/<username>")
def mypage(username):
    username = mongo.db.user.find_one(
        {"username": session["user"]})

    if session["user"]:
        print(username)
        return render_template("mypage.html", username=username)

    return redirect(url_for("login"))


@app.route("/login", methods=["GET","POST"])
def login():
    """
        Login function
    """
    if request.method == "POST":
        get_user = mongo.db.user.find_one(
            {"username": request.form.get("username")}
        )
    
        if get_user:
            if check_password_hash(get_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                a = request.form.get("username")
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for("welcome", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password!")
            return redirect(url_for("login"))

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
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.insert(signup)

        #Add user into cookie
        session["user"] = request.form.get("username")
        flash("We are glad that you joined us!")
        return redirect(url_for("welcome"))

    return render_template("signup.html")


@app.route("/logout")
def logout():
    """
        Log out
    """
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("welcome"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)