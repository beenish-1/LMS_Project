from flask import Flask, render_template, request, redirect, session, flash
from backend import create_account, login_user

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        action = request.form.get("action")
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if action=="create":
            if create_account(name,email,password):
                flash("Account created successfully! Login now.","success")
            else:
                flash("Email already exists","error")
            return redirect("/")
        elif action=="login":
            user = login_user(email,password)
            if user:
                session["user"] = user
                return redirect("/dashboard")
            else:
                flash("Invalid login or account doesn't exist!","error")
                return redirect("/")
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    user = session["user"]
    return render_template("dashboard.html", user=user)

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully","success")
    return redirect("/")
