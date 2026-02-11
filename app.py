from flask import Flask, render_template, request, session
import random


app = Flask(__name__)
app.secret_key = "super-secret-key"  # change later
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        contact = request.form["contact"]
        return f"OTP will be sent to {contact}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)



app = Flask(__name__)
app.secret_key = "super-secret-key"  # change later