from flask import Flask , request, Response, url_for, session, redirect, render_template

app = Flask(__name__)
app.secret_key = "mysecretkey"
persondatas = {
    'arsalan': 'AI Data Science Engineer',
    'usman': 'MBBS Doctor',
    'mazhar': 'Business Man',
    'asim': 'Private Job'
}

@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
        username = request.form.get("username")
        password = request.form.get("password")

        userData = {
             'arsalan':'1181',
             'asim': '2005',
             'usman': '2004',
             'mazhar':'2006'
        }
        
        if username in userData and password == userData[username]:
             return render_template("welcome.html", name = username, data=persondatas)
        else:
            return "in-valid username or password"
        
@app.route("/logout")
def logout():
    return redirect(url_for("login"))

