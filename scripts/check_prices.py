import os
import requests

ACCESS_TOKEN = os.getenv("ML_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise Exception("ML_ACCESS_TOKEN não configurado no GitHub Secrets")

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

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    print("📡 Status:", response.status_code)

    if response.status_code != 200:
        print("❌ Erro:", response.text)
        continue

    data = response.json()

    results = data.get("results", [])
    if not results:
        print("❌ Nenhum resultado encontrado")
        continue

    produto_api = results[0]

    title = produto_api.get("title", "N/A")
    price = produto_api.get("price", 999999)

    print("\n📌 Produto:", title)
    print("💰 Preço atual:", price)
    print("🎯 Preço alvo:", produto["target_price"])

    if price <= produto["target_price"]:
        print("🚨 PREÇO BAIXOU!")
    else:
        print("📈 Ainda acima do alvo")

print("\n✅ Script terminou")
