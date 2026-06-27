import requests

ACCESS_TOKEN = "APP_USR-5163526809822265-062620-b937f5e41a5e6fb0f04c40b044bd5363-77300613"

def buscar_produto(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    print("\n🔎 Produto:", query)
    print("📡 Status:", response.status_code)

    if response.status_code != 200:
        print("❌ Erro:", response.text)
        return None

    data = response.json()
    item = data["results"][0]

    return {
        "title": item["title"],
        "price": item["price"],
        "link": item["permalink"]
    }


produto = buscar_produto("ssd 1tb")

print("\n📌 Produto:", produto["title"])
print("💰 Preço:", produto["price"])
print("🔗 Link:", produto["link"])
