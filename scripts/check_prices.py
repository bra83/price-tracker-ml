import json
import requests

print("🚀 Script iniciou")

with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print("📦 Produtos carregados:", products)

for p in products:
    print("🔎 Consultando:", p)

print("✅ Script terminou")
