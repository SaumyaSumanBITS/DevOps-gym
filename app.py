from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

DB = "aceest.db"

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            weight REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- UI ROUTES ----------
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

# ---------- API ROUTES ----------

# Home API
@app.route("/api")
def api_home():
    return jsonify({
        "message": "ACEest API Running",
        "endpoints": [
            "/api/clients",
            "/api/clients/<id>",
            "/api/bmi",
            "/health"
        ]
    })

# ---------- CREATE ----------
@app.route("/api/clients", methods=["POST"])
def add_client():
    data = request.json

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clients(name, age, weight) VALUES (?,?,?)",
        (data["name"], data["age"], data["weight"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Client added"})

# ---------- READ ALL ----------
@app.route("/api/clients", methods=["GET"])
def get_clients():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients")
    rows = cur.fetchall()

    conn.close()

    clients = [
        {"id": r[0], "name": r[1], "age": r[2], "weight": r[3]}
        for r in rows
    ]

    return jsonify(clients)

# ---------- READ ONE ----------
@app.route("/api/clients/<int:id>", methods=["GET"])
def get_client(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients WHERE id=?", (id,))
    row = cur.fetchone()

    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "weight": row[3]
        })

    return jsonify({"error": "Client not found"}), 404

# ---------- UPDATE ----------
@app.route("/api/clients/<int:id>", methods=["PUT"])
def update_client(id):
    data = request.json

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "UPDATE clients SET name=?, age=?, weight=? WHERE id=?",
        (data["name"], data["age"], data["weight"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Client updated"})

# ---------- DELETE ----------
@app.route("/api/clients/<int:id>", methods=["DELETE"])
def delete_client(id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("DELETE FROM clients WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Client deleted"})

# ---------- BMI ----------
@app.route("/api/bmi")
def bmi():
    try:
        height = float(request.args.get("height"))
        weight = float(request.args.get("weight"))
        h = height / 100
        bmi_value = weight / (h * h)
        return jsonify({"BMI": round(bmi_value, 2)})
    except:
        return jsonify({"error": "Invalid input"}), 400

# ---------- HEALTH ----------
@app.route("/health")
def health():
    return jsonify({"status": "OK"})

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
