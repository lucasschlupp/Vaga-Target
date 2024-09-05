faturamento = [
    {"estado": "SP", "faturamento": 67836.43},
    {"estado": "RJ", "faturamento": 36678.66},
    {"estado": "MG", "faturamento": 29229.88},
    {"estado": "ES", "faturamento": 27165.48},
    {"estado": "Outros", "faturamento": 19849.53}
]

total_fat = sum(item["faturamento"] for item in faturamento)

for item in faturamento:
    porcentagem = (item["faturamento"] / total_fat) * 100
    print(f"Estado: {item['estado']}, {porcentagem:.2f}% do total mensal.")