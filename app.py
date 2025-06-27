from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

BASE_DIR = "notes"
os.makedirs(BASE_DIR, exist_ok=True)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ note_id }}</title>
    <meta charset="utf-8">
</head>
<body>
    <h3>Note: {{ note_id }}</h3>
    <form method="POST">
        <textarea name="content" style="width:100%;height:90vh;">{{ content }}</textarea>
        <br/>
        <button type="submit">Salvar</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return '<a href="/minhanota">Clique para abrir uma nota</a>'

@app.route("/<note_id>", methods=["GET", "POST"])
def note(note_id):
    file_path = os.path.join(BASE_DIR, f"{note_id}.txt")

    if request.method == "POST":
        content = request.form.get("content", "")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    return render_template_string(TEMPLATE, note_id=note_id, content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
