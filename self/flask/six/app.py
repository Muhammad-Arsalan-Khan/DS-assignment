from flask import Flask, redirect , url_for, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route("/", methods=["GET"])
def home():
    return render_template("base.html")



@app.route("/feedback", methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        username = request.form.get("username")
        message = request.form.get("message")  
        if not username or not message:
            message = "plz enter the field."   
            flash(message)
            return redirect(url_for('feedback'))
        flash(f'Thank you {username} for your feedback!')
        return render_template("thankyou.html", username = username , message = message)
    
    return render_template("feedback.html")