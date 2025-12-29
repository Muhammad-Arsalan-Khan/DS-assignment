from flask import Flask, redirect , url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("base.html")

@app.route("/feedback", methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        username = request.form.get("username")
        message = request.form.get("message")     # ===> agara kuch ni aye ga tu ya get err ni none bejay ga jis se web crash ni hogi
        #message = request.form["message"]("message")     # ===> agara kuch ni aye ga tu ya key[] err  bejay gi jis se web crash hogi
        print(username, message)
        return render_template("thankyou.html", username = username , message = message)
    
    return render_template("feedback.html")