from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ML Proxy OK"

@app.route("/price")
def price():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "missing query"}), 400

    url = "https://api.mercadolibre.com/sites/MLB/search"
    r = requests.get(url, params={"q": query})

    data = r.json()
    results = data.get("results", [])

    if not results:
        return jsonify({"error": "no results"}), 404

    item = results[0]

    return jsonify({
        "title": item["title"],
        "price": item["price"],
        "link": item["permalink"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
