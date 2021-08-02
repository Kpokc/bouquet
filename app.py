import os
import random
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
    likes = list(mongo.db.likes.find())
    comments = list(mongo.db.comments.find())

    # list of likes id
    most_liked_post = []
    i = 0
    for post in posts:
        # (nl to br) replace new line with page break
        post["content"] = post["content"].replace('\n', '<br />')
        # \t to tab (8 spaces)
        tab = "&nbsp;" * 8
        post["content"] = post["content"].replace('\t', tab)
        most_liked_post.insert(i, [str(post["_id"]), 0])
        i =+ 1

    # list of comments id
    most_commented_post = most_liked_post

    # count likes for each post
    for number in range(len(most_liked_post)):
        for like in likes:
            if like["post_id"] == most_liked_post[number][0]:
                most_liked_post[number][1] += 1

    # Sort likes by second column
    most_liked_post = sorted(most_liked_post, key=lambda x:x[1])
    most_liked = most_liked_post[len(most_liked_post)-1][0]
    print(most_commented_post)
    # count comments for each post
    for number in range(len(most_commented_post)):
        for comment in comments:
            if comment["post_id"] == most_commented_post[number][0]:
                most_commented_post[number][1] += 1

    # sort comments by second column
    most_commented_post = sorted(most_commented_post, key=lambda x:x[1])
    most_commented = most_commented_post[len(most_commented_post)-1][0]

    # get random post 
    show_random_post = random.choice(most_commented_post)
    random_post = show_random_post[0]


    categories = list(mongo.db.categories.find())
    users = list(mongo.db.user.find())
    dislikes = list(mongo.db.dislikes.find())
    pinned = list(mongo.db.pinned.find())
    return render_template("cards.html", posts=posts, categories=categories, users=users, likes=likes, dislikes=dislikes, 
                                        pinned=pinned, most_liked=most_liked, most_commented=most_commented, random_post=random_post)


@app.template_filter('check_likes')
def check_likes(s):
    """
        this filter returns total count of likes for each post
    """
    like_count = 0
    likes = list(mongo.db.likes.find())
    
    for like in likes:
        if like["post_id"] == s:
            like_count += 1

    return like_count


@app.template_filter('check_dislikes')
def check_dislikes(s):
    """
        this filter returns total count of dislikes for each post
    """
    dislike_count = 0
    dislikes = list(mongo.db.dislikes.find())
    
    for dislike in dislikes:
        if dislike["post_id"] == s:
            dislike_count += 1

    return dislike_count


@app.template_filter('check_comments')
def check_comments(s):
    """
        this filter returns total count of comments for each post
    """
    comments_count = 0
    comments = list(mongo.db.comments.find())
    
    for comment in comments:
        if comment["post_id"] == s:
            comments_count += 1

    return comments_count


@app.route("/search", methods=["GET", "POST"])
def search():
    """
        Search troughout posts title or content
    """
    # get search word from form
    query = request.form.get("query")
    posts = list(mongo.db.post.find())

    # find word in post or title, if found add post to found list
    found = []
    for post in posts:
        if query.lower() in post["content"].lower() or query.lower() in post["title"].lower():
            found.append(post)

    likes = list(mongo.db.likes.find())
    comments = list(mongo.db.comments.find())

    # list of likes id
    most_liked_post = []
    i = 0
    for post in posts:
        # (nl to br) replace new line with page break
        post["content"] = post["content"].replace('\n', '<br />')
        # \t to tab (8 spaces)
        tab = "&nbsp;" * 8
        post["content"] = post["content"].replace('\t', tab)
        most_liked_post.insert(i, [str(post["_id"]), 0])
        i =+ 1

    # below same code as in welcome route
    most_commented_post = most_liked_post
    for number in range(len(most_liked_post)):
        for like in likes:
            if like["post_id"] == most_liked_post[number][0]:
                most_liked_post[number][1] += 1


    most_liked_post = sorted(most_liked_post, key=lambda x:x[1])
    most_liked = most_liked_post[len(most_liked_post)-1][0]

    for number in range(len(most_commented_post)):
        for comment in comments:
            if comment["post_id"] == most_commented_post[number][0]:
                most_commented_post[number][1] += 1

    most_commented_post = sorted(most_commented_post, key=lambda x:x[1])
    most_commented = most_commented_post[len(most_commented_post)-1][0]

    show_random_post = random.choice(most_commented_post)
    random_post = show_random_post[0]

    categories = list(mongo.db.categories.find())
    users = list(mongo.db.user.find())
    dislikes = list(mongo.db.dislikes.find())
    pinned = list(mongo.db.pinned.find())
    return render_template("search.html", posts=found, categories=categories, users=users, likes=likes, dislikes=dislikes, 
                                        pinned=pinned, most_liked=most_liked, most_commented=most_commented, random_post=random_post)


@app.route("/read_post/<post_id>")
def read_post(post_id):
    """
        Read single post on a new page
    """
    post_to_read = mongo.db.post.find_one(
        {"_id": ObjectId(post_id)}
    )

    # (nl to br) replace new line with page break
    post_to_read["content"] = post_to_read["content"].replace('\n', '<br />')
    # \t to tab (8 spaces)
    tab = "&nbsp;" * 8
    post_to_read["content"] = post_to_read["content"].replace('\t', tab)


    posts = list(mongo.db.post.find().sort("time", -1))
    likes = list(mongo.db.likes.find())
    comments = list(mongo.db.comments.find())

    for comment in comments:
        # (nl to br) replace new line with page break
        comment["comment"] = comment["comment"].replace('\n', '<br />')
        # \t to tab (8 spaces)
        tab = "&nbsp;" * 8
        comment["comment"] = comment["comment"].replace('\t', tab)

    most_liked_post = []
    i = 0
    for post in posts:
        # (nl to br) replace new line with page break
        post["content"] = post["content"].replace('\n', '<br />')
        # \t to tab (8 spaces)
        tab = "&nbsp;" * 8
        post["content"] = post["content"].replace('\t', tab)

        most_liked_post.insert(i, [str(post["_id"]), 0])
        i =+ 1
    
    # below same code as in welcome route
    most_commented_post = most_liked_post
    for number in range(len(most_liked_post)):
        for like in likes:
            if like["post_id"] == most_liked_post[number][0]:
                most_liked_post[number][1] += 1
    

    most_liked_post = sorted(most_liked_post, key=lambda x:x[1])
    most_liked = most_liked_post[len(most_liked_post)-1][0]

    for number in range(len(most_commented_post)):
        for comment in comments:
            if comment["post_id"] == most_commented_post[number][0]:
                most_commented_post[number][1] += 1


    most_commented_post = sorted(most_commented_post, key=lambda x:x[1])
    most_commented = most_commented_post[len(most_commented_post)-1][0]

    show_random_post = random.choice(most_commented_post)
    random_post = show_random_post[0]
                
    # (nl to br) replace new line with page break
    post["content"] = post["content"].replace('\n', '<br />')
    # \t to tab (8 spaces)
    tab = "&nbsp;" * 8
    post["content"] = post["content"].replace('\t', tab)

    categories = list(mongo.db.categories.find())
    users = list(mongo.db.user.find())
    dislikes = list(mongo.db.dislikes.find())
    pinned = list(mongo.db.pinned.find())
    return render_template("read_post.html", posts=posts, post_to_read=post_to_read, categories=categories, users=users, comments=comments, likes=likes, dislikes=dislikes, pinned=pinned,
                                            most_liked=most_liked, most_commented=most_commented, random_post=random_post)


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

        #prepare query variable
        post = {
            "user_id": str(user_id["_id"]), # add user id
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now,
        }
        # add post to db 
        mongo.db.post.insert_one(post)
        flash("Post Added!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
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
        #prepare query variable
        post = {
            "user_id": str(user_id["_id"]), # add user id
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "date" : today.strftime("%B %d, %Y"),
            "time": now,
        }
        mongo.db.post.update({"_id": ObjectId(post_id)}, post)
        flash("Post Updated!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img

        #redirect to reade recently added post
        return redirect(url_for("read_post", post_id=post_id))

    # redirect to edit post page
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
    flash("Post Deleted!")
    flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
    return redirect(url_for("welcome"))


@app.route("/like/<post_id>/<page>", methods=["GET","POST"])
def like(post_id, page):
    """
        Like post
    """
    insert = True
    dislikes = list(mongo.db.dislikes.find())
    likes = list(mongo.db.likes.find())

    if len(likes) == 0:
        # Add to likes if table is empty.
        like = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.likes.insert_one(like)

    
    # Check if there is data in the likes table. 
    if len(likes) > 0:
        for like in likes:
            # Check if this post has been liked by current user.
            if like["username"] == session["user"] and like["post_id"] == post_id:
                like_id = str(like["_id"])
                insert = False
            else:
                insert = True
    
    if insert == False:
        # Delete like from db
        mongo.db.likes.delete_one({
            "_id": ObjectId(like_id)
        })

    # Check if user had disliked this post before if so delete
    if len(dislikes) > 0:
        for dislike in dislikes:
            if dislike["username"] == session["user"] and dislike["post_id"] == post_id:
                mongo.db.dislikes.delete_one({
                    "_id": ObjectId(dislike["_id"])
                })

    if insert == True and len(likes) > 0:
        # Add to likes if table is empty.
        like = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.likes.insert_one(like)
    
    # Get user info by his sessions name 
    username = mongo.db.user.find_one(
        {"username": session["user"]}
    )

    # Check if comment or post was liked
    post = mongo.db.comments.find_one(
        {"_id": ObjectId(post_id)}
    )
    # if comment then get post id from comment row
    if post:
        post_id = post["post_id"]
    
    # return to page where like btn clicked
    if page == "welcome":
        return redirect(url_for("welcome"))
    if page == "post":
        return redirect(url_for("read_post", post_id=post_id))
    if page == "mypage":
        return redirect(url_for("mypage", username=username))

    # return nothing
    return ('', 204)


@app.route("/dislike/<post_id>/<page>", methods=["GET","POST"])
def dislike(post_id, page):
    """
        Dislike post
    """
    insert = True

    dislikes = list(mongo.db.dislikes.find())
    likes = list(mongo.db.likes.find())

    if len(dislikes) == 0:
        # Add to dislikes if table is empty.
        dislike = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.dislikes.insert_one(dislike)

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
                dislike_id = str(dislike["_id"])
                insert = False
            else:
                insert = True
    
    if insert == False:
        # Delete like from db
        mongo.db.dislikes.delete_one({
            "_id": ObjectId(dislike_id)
        })
    
    if insert == True and len(dislikes) > 0:
        # Add to dislikes if table is empty.
        dislike = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.dislikes.insert_one(dislike)
    
    # Get user info by his sessions name 
    username = mongo.db.user.find_one(
        {"username": session["user"]}
    )

    # Check if comment or post was liked
    post = mongo.db.comments.find_one(
        {"_id": ObjectId(post_id)}
    )
    # if comment then get post id from comment row
    if post:
        post_id = post["post_id"]
    
    # redirect to page where dislike btn clicked
    if page == "welcome":
        return redirect(url_for("welcome"))
    if page == "post":
        return redirect(url_for("read_post", post_id=post_id))
    if page == "mypage":
        return redirect(url_for("mypage", username=username))

    # return nothing
    return ('', 204)


@app.route("/pinned/<post_id>/<page>", methods=["GET","POST"])
def pinned(post_id, page):
    """
        Pin post
    """
    insert = True
    
    pinned = list(mongo.db.pinned.find())
    
    #Check if there is data in the pined table. 
    if len(pinned) > 0:
        for pin in pinned:
            # Check if this post has been pined by current user.
            if pin["username"] == session["user"] and pin["post_id"] == post_id:
                # Delete from pinned.
                mongo.db.pinned.delete_one({
                    "_id": ObjectId(pin["_id"])
                })
                insert = False


    if insert == True:
        # Add to pinned if not in the table.
        pin = ({
            "username": session["user"],
            "post_id": post_id
        })
        mongo.db.pinned.insert_one(pin)
    
    # Get user info by his sessions name 
    username = mongo.db.user.find_one(
        {"username": session["user"]}
    )

    # Check if comment or post was liked
    post = mongo.db.comments.find_one(
        {"_id": ObjectId(post_id)}
    )
    # if comment then get post id from comment row
    if post:
        post_id = post["post_id"]

    # redirect to page where pinned btn clicked
    if page == "welcome":
        return redirect(url_for("welcome"))
    if page == "post":
        return redirect(url_for("read_post", post_id=post_id))
    if page == "mypage":
        return redirect(url_for("mypage", username=username))

    # return nothing
    return ('', 204)


@app.template_filter('check_pin')
def check(s):
    """
        this filter is checking if post was pinned by current user
    """
    pinned = list(mongo.db.pinned.find())
    pin_id = "notok"

    # s[0:s.find("/")] -- username
    # s[s.find("/")+1:len(s)] -- post_id
    if len(pinned) > 0:
        for pin in pinned:
            if pin["username"] == s[0:s.find("/")]:
                if pin["post_id"] == s[s.find("/")+1:len(s)]:
                    pin_id = "ok"
    # if id ok btn color blue else standart
    return pin_id


@app.template_filter('check_like')
def check2(s):
    """
        this filter is checking if post was pinned by current user
    """
    likes = list(mongo.db.likes.find())
    like_id = "not_liked"

    # s[0:s.find("/")] -- username
    # s[s.find("/")+1:len(s)] -- post_id
    if len(likes) > 0:
        for like in likes:
            if like["username"] == s[0:s.find("/")]:
                if like["post_id"] == s[s.find("/")+1:len(s)]:
                    like_id = "ok"
    # if id ok btn color blue else standart
    return like_id


@app.template_filter('check_dislike')
def check3(s):
    """
        this filter is checking if post was pinned by current user
    """
    likes = list(mongo.db.dislikes.find())
    like_id = "not_disliked"

    # s[0:s.find("/")] -- username
    # s[s.find("/")+1:len(s)] -- post_id
    if len(likes) > 0:
        for like in likes:
            if like["username"] == s[0:s.find("/")]:
                if like["post_id"] == s[s.find("/")+1:len(s)]:
                    like_id = "ok"
    # if id ok btn color blue else standart
    return like_id


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
        flash("Comment Added!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
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

        # prepare comment variable
        comment = ({
            "user_id": str(user_id["_id"]),
            "post_id": old_comment["post_id"],
            "comment": request.form.get("comment"),
            "date" : old_comment["date"],
            "time": old_comment["time"]
        })
        flash("Comment Updated!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, comment)

    post_id = mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)}
    )
    # redirect to commented post
    return redirect(url_for("read_post", post_id=post_id["post_id"]))


@app.route("/delete_comment/<comment_id>", methods=["GET","POST"])
def delete_comment(comment_id):
    """
        Delete comment
    """
    comment = mongo.db.comments.find_one(
        {"_id": ObjectId(comment_id)}
    )

    #Delete post
    mongo.db.comments.remove({
        "_id":ObjectId(comment_id)
    })
    flash("Comment Deleted!")
    flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
    # redirect to post where comment was deleted
    return redirect(url_for("read_post", post_id=comment["post_id"]))


@app.route("/mypage/<username>")
def mypage(username):
    username = mongo.db.user.find_one(
        {"username": session["user"]})

    if session["user"]:
        posts = list(mongo.db.post.find().sort("time", -1))
        likes = list(mongo.db.likes.find())
        comments = list(mongo.db.comments.find())
        categories = list(mongo.db.categories.find())
        users = list(mongo.db.user.find())
        dislikes = list(mongo.db.dislikes.find())
        pinned = list(mongo.db.pinned.find())

        for post in posts:
            # (nl to br) replace new line with page break
            post["content"] = post["content"].replace('\n', '<br />')
            # \t to tab (8 spaces)
            tab = "&nbsp;" * 8
            post["content"] = post["content"].replace('\t', tab)

        return render_template("mypage.html", username=username, posts=posts, categories=categories, users=users, likes=likes, dislikes=dislikes, 
                                        pinned=pinned, comments=comments)

    return redirect(url_for("login"))


@app.route("/delete_comment_mypage/<comment_id>", methods=["GET","POST"])
def delete_comment_mypage(comment_id):
    """
        Delete comment from "My Page"
    """
    username = mongo.db.user.find_one(
        {"username": session["user"]})

    #Delete post
    mongo.db.comments.remove({
        "_id":ObjectId(comment_id)
    })
    flash("Comment Deleted!")
    flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success pick
    # redirect to my page
    return redirect(url_for("mypage", username=username))


@app.route("/edit_comment_mypage/<comment_id>", methods=["GET","POST"])
def edit_comment_mypage(comment_id):
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
        flash("Comment Updated!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, comment)
    
    # redirect to my page
    return redirect(url_for("mypage", username=user_id))


@app.route("/delete_post_mypage/<post_id>")
def delete_post_mypage(post_id):
    """
        Delete post
    """
    user_id = mongo.db.user.find_one(
        {"username": session["user"]}
    )
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
    flash("Post Deleted!")
    flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
    # redirect to my page
    return redirect(url_for("mypage", username=user_id))


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
                #a = request.form.get("username")
                flash("Welcome {}".format(request.form.get("username")))
                flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
                return redirect(url_for("welcome", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password!")
                flash("https://img.icons8.com/color/144/000000/cancel--v1.png") # error img
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password!")
            flash("https://img.icons8.com/color/144/000000/cancel--v1.png") # error img
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
            flash("https://img.icons8.com/color/144/000000/cancel--v1.png") # error img
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.insert(signup)

        #Add user into cookie
        session["user"] = request.form.get("username")
        flash("Thanks for joining!")
        flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success pick
        return redirect(url_for("welcome"))

    return render_template("signup.html")


@app.route("/contact")
def contact():
    """
        Contact
    """
    
    return render_template("contact.html")


@app.route("/logout")
def logout():
    """
        Log out
    """
    flash("Logged Out!")
    flash("https://img.icons8.com/ultraviolet/120/000000/ok.png") # success img
    session.pop("user")
    return redirect(url_for("welcome"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)