from flask import Flask, render_template
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)  # allow CORS for all domains on all routes.


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/forecast")
def forecast():
    return render_template("forecast.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
