import requests

products = [
    {
        "name": "SSD 1TB",
        "query": "ssd 1tb",
        "target_price": 300
    }
]

for produto in products:
    print("\n🔎 Produto:", produto["name"])

    url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto['query']}"

    response = requests.get(url)

    print("📡 Status:", response.status_code)

    if response.status_code != 200:
        print("❌ Erro:", response.text)
        continue

    data = response.json()

    results = data.get("results", [])

    if not results:
        print("❌ Nenhum resultado")
        continue

    item = results[0]

    print("\n📌 Produto:", item.get("title"))
    print("💰 Preço:", item.get("price"))

print("\n✅ Script terminou")
