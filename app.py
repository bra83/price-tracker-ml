from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json"
}

@app.route("/")
def home():
    return {"status": "ML Proxy OK"}

@app.route("/search")
def search():
    q = request.args.get("q")

    if not q:
        return {"error": "missing query param ?q="}, 400

    url = "https://api.mercadolibre.com/sites/MLB/search"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params={"q": q},
            timeout=10
        )

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

    except Exception as e:
        return {"error": "exception", "detail": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
