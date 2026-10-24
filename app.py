from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    previews = sorted([f for f in os.listdir(BASE_DIR) if f.startswith("preview_") and f.endswith(".png")])
    has_video = os.path.exists(os.path.join(BASE_DIR, "lily_3d_botanical_animation.mp4"))
    return render_template("index.html", previews=previews, has_video=has_video)

@app.route("/video/<path:filename>")
def video(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route("/preview/<path:filename>")
def preview(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
