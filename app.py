from flask import Flask, render_template, request
from scam_detector import is_scam

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        msg = request.form.get("message")
        scam, reason = is_scam(msg)
        result = {"scam": scam, "reason": reason, "text": msg}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)