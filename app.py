import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/a")
def hello():
    return "<h1>Hellocc</h1>"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)