import json
import requests

print("🚀 Script iniciou")

# 1. carregar produtos
with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print("📦 Produtos carregados:", products)

# 2. função que busca preço no Mercado Livre
def get_price(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    print("\n🌐 URL:", url)
    print("📡 Status code:", r.status_code)
    print("📄 Resposta bruta:", r.text[:300])

    data = r.json()

    if "results" not in data or len(data["results"]) == 0:
        print("❌ Nenhum resultado retornado pela API")
        return "N/A", 999999

    first = data["results"][0]
    title = first["title"]
    price = first["price"]

    return title, price

# 3. loop nos produtos
for p in products:
    print("\n🔎 Produto:", p["name"])

    title, price = get_price(p["query"])

    print("📌 Título encontrado:", title)
    print("💰 Preço atual:", price)
    print("🎯 Preço alvo:", p["target_price"])

    if price <= p["target_price"]:
        print("🚨 PREÇO BAIXOU!")
    else:
        print("📈 Ainda acima do alvo")

print("\n✅ Script terminou")
