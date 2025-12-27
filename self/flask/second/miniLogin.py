from flask import Flask , request, Response, url_for, session, redirect

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid password", mimetype="text/plain")
    return '''
      <h2>Login page<h2/>
      <form method="POST">
       Username : <input type="text" name="username"><br>
       Password : <input type="text" name="password"><br>
       <input type="submit" value="login">
      <form/>
'''

@app.route("/welcome")
def welcome():
    if 'user' in session:
        return f'''
          <h2>Welcome {session["user"]}!<h2/>
          <a href={url_for("logout")}>Logout<a/>
'''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

