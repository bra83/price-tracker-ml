from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ML Proxy OK"}

@app.route("/search")
def search():
    q = request.args.get("q")

    if not q:
        return {"error": "missing query param ?q="}, 400

    url = "https://api.mercadolibre.com/sites/MLB/search"
    response = requests.get(url, params={"q": q})

    if response.status_code != 200:
        return {
            "error": "api error",
            "status": response.status_code,
            "detail": response.text
        }, 500

    data = response.json()
    results = data.get("results", [])

    if not results:
        return {"error": "no results", "query": q}

    item = results[0]

    return {
        "title": item.get("title"),
        "price": item.get("price"),
        "url": item.get("permalink")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
