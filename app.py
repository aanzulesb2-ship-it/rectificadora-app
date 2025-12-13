from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

# Google Search Console verification
@app.route("/google842d86f7ffbc34aa.html")
def google_verify():
    return send_file(os.path.join(os.getcwd(), "google842d86f7ffbc34aa.html"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


