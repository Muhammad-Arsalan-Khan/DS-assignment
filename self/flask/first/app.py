from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def home():
    return ("hello arsalan is first web page using python & flask")

@app.route("/about")
def about():
    return "this is about page"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "you send the data"
    else:
        return "you view the data"
