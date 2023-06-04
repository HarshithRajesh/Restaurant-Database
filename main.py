from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)