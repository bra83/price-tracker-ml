import requests

# =========================
# FUNÇÃO: busca preço no Mercado Livre
# =========================
def get_price(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(f"\n🌐 URL: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print(f"📡 Status code: {response.status_code}")
        print(f"📄 Resposta bruta (primeiros 200 chars): {response.text[:200]}")

        # Se API bloqueou ou deu erro
        if response.status_code != 200:
            print("❌ API bloqueada ou erro de requisição")
            return "N/A", 999999

        data = response.json()

        # Segurança caso não venha "results"
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


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    print("🚀 Script iniciou")

    products = [
        {
            "name": "SSD 1TB",
            "query": "ssd 1tb",
            "target_price": 300
        }
    ]

    print(f"📦 Produtos carregados: {products}")

    for p in products:
        print(f"\n🔎 Produto: {p['name']}")

        title, price = get_price(p["query"])

        print(f"\n📌 Título encontrado: {title}")
        print(f"💰 Preço atual: {price}")
        print(f"🎯 Preço alvo: {p['target_price']}")

        if price <= p["target_price"]:
            print("🚨 OPORTUNIDADE! Preço abaixo do alvo")
        else:
            print("📈 Ainda acima do alvo")

    print("\n✅ Script terminou")
