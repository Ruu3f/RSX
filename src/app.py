from freeGPT import Client
from flask import Flask, render_template
from duckduckgo_search import DDGS


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search/<query>", methods=["GET"])
def search(query):
    results = list(DDGS().text(query, region="en-us", safesearch="Off", timelimit="y"))
    return render_template("search_results.html", query=query, results=results)


@app.route("/api/chat/<query>", methods=["GET"])
def api(query):
    resp = Client.create_completion("gpt4", query)

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)