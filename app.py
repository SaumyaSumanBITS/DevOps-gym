from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))
    else:
        return "Invalid login"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)