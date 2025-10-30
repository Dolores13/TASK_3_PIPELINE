
from flask import Flask, request

app = Flask(__name__)
FICHERO = "users.txt"

HTML_FORM = """
<!DOCTYPE html>
<html>
<title>Contest Registration</title>
<h1>Contest Registration</h1>
<form method="post" action="/register">
    <label>Name:</label><br>
    <input type="text" name="name" required><br>
    <label>Age:</label><br>
    <input type="number" name="age" required><br>
    <button type="submit">Register</button>
</form>
<p><a href="/list"> See all registrations </a></p>
</html>
"""
def save_registration(name, age):
    try:
        with open(FICHERO, 'a') as f:
            f.write(f"{name},{age}\n")
    except Exception as e:
        print(f"Error saving registration: {e}")
        return False
    
@app.route('/', methods=['GET'])
def home():
    return HTML_FORM

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    if not name or not age.isdigit():
        return '<p style="color:red">Invalid data. <a href="/">Back</a></p>'
    save_registration(name, int(age))
    return '<p style="color:green">Saved! <a href="/">Back</a> | <a href="/list">See list</a></p>'

@app.route("/list", methods=["GET"])
def list_users():
    filas = []
    try:
        with open(FICHERO, "r", encoding="utf-8") as f:
            filas = f.read().strip().splitlines()
    except FileNotFoundError:
        pass
    tabla = "<table border=1 cellpadding=6><tr><th>Name</th><th>Age</th></tr>"
    for row in filas:
        name, age = row.split(",", 1)
        tabla += f"<tr><td>{name}</td><td>{age}</td></tr>"
    tabla += "</table>" if filas else "<p>No registrations yet.</p>"
    return f"<h1>Registrations</h1>{tabla}<p><a href='/'>Back to form</a></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)