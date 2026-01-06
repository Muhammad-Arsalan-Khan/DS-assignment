from flask import Flask, redirect , url_for, render_template, request , flash
from forms import RegistrationForm
app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f'Account created for {username}!', 'success')
        # Here you would typically save the user to the database
        return redirect(url_for('success', username=username))
    return render_template("register.html", form=form)

@app.route("/success/<username>")
def success(username):
    return render_template("success.html", username=username)