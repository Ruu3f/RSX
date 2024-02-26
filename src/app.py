from flask import Flask, render_template
from duckduckgo_search import DDGS

app = Flask(__name__)
results = None


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search/<q>", methods=["GET"])
def search(q):
    global results
    results = list(DDGS().text(q, region="en-us", safesearch="Off", timelimit="y"))
    return render_template("results.html", q=q, results=results)


@app.route("/summary", methods=["GET"])
def summary():
    return "WIP"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
