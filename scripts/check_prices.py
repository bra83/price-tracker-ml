import requests

API_URL = "https://api.mercadolibre.com/sites/MLB/search"


def get_price(query):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    params = {
        "q": query
    }

    try:
        response = requests.get(API_URL, params=params, headers=headers, timeout=10)

        print(f"\n🌐 URL: {response.url}")
        print(f"📡 Status code: {response.status_code}")
        print(f"📄 Resposta bruta (primeiros 300 chars): {response.text[:300]}")

        if response.status_code != 200:
            print("❌ API bloqueada ou erro de requisição")
            return "N/A", 999999

        data = response.json()

        # proteção contra resposta inválida
        if "results" not in data or not data["results"]:
            print("❌ Nenhum resultado retornado pela API")
            return "N/A", 999999

        first = data["results"][0]

        title = first.get("title", "N/A")
        price = first.get("price", 999999)

        return title, price

    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return "N/A", 999999


def main():
    print("🚀 Script iniciou")

    produtos = [
        {"name": "SSD 1TB", "query": "ssd 1tb", "target_price": 300}
    ]

    print(f"📦 Produtos carregados: {produtos}")

    for p in produtos:
        print(f"\n🔎 Produto: {p['name']}")

        title, price = get_price(p["query"])

        print(f"\n📌 Título encontrado: {title}")
        print(f"💰 Preço atual: {price}")
        print(f"🎯 Preço alvo: {p['target_price']}")

        if price <= p["target_price"]:
            print("🔥 ABAIXOU DO PREÇO!")
        else:
            print("📈 Ainda acima do alvo")

    print("\n✅ Script terminou")


if __name__ == "__main__":
    main()
