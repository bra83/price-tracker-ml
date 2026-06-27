import requests
import os

# 🔐 Coloque seu token aqui OU use variável de ambiente
ACCESS_TOKEN = os.getenv("MELI_ACCESS_TOKEN") or "APP_USR-5163526809822265-062620-b937f5e41a5e6fb0f04c40b044bd5363-77300613"

PRODUCTS = [
    {
        "name": "SSD 1TB",
        "query": "ssd 1tb",
        "target_price": 300
    }
]

def buscar_produto(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    print("\n🔎 Produto:", query)
    print("🌐 URL:", url)
    print("📡 Status code:", response.status_code)

    if response.status_code != 200:
        print("❌ Erro na API:", response.text)
        return None

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        print("❌ Nenhum resultado")
        return None

    item = data["results"][0]

    return {
        "title": item["title"],
        "price": item["price"],
        "link": item["permalink"]
    }


def main():
    print("🚀 Script iniciou")

    for product in PRODUCTS:
        result = buscar_produto(product["query"])

        if not result:
            print("📌 Produto não encontrado")
            continue

        print("📌 Título:", result["title"])
        print("💰 Preço atual:", result["price"])
        print("🎯 Preço alvo:", product["target_price"])

        if result["price"] <= product["target_price"]:
            print("🔥 PREÇO BAIXOU! ALERTA!")
            print(result["link"])
        else:
            print("📈 Ainda acima do alvo")

    print("\n✅ Script terminou")


if __name__ == "__main__":
    main()
