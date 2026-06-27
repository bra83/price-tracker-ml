from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "missing query"}), 400

    url = "https://api.mercadolibre.com/sites/MLB/search"

    r = requests.get(url, params={"q": query}, headers=HEADERS)

    return jsonify(r.json())


@app.route("/")
def home():
    return "ML Proxy OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
