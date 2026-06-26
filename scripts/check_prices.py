import requests
import json

with open("data/products.json", "r") as f:
    products = json.load(f)

for p in products:
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={p['query']}"
    res = requests.get(url).json()

    results = res.get("results", [])

    if not results:
        continue

    best = results[0]
    price = best["price"]
    title = best["title"]
    link = best["permalink"]

    print(f"\nProduto: {p['name']}")
    print(f"Melhor oferta: {title}")
    print(f"Preço: R$ {price}")
    print(f"Link: {link}")

    if price <= p["target_price"]:
        print("🔥 ALERTA: abaixo do preço alvo!")
