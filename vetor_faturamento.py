fat_diario = {
    "Janeiro": [{"dia": 1, "faturamento": 1300.00},
                {"dia": 2, "faturamento": 1500.00},
                {"dia": 3, "faturamento": 1700.00},
                {"dia": 3, "faturamento": 2000.00},
                {"dia": 3, "faturamento": 1800.00}],
    "Fevereiro": [{"dia": 1, "faturamento": 2000.00}]
}

def menor_valor(mes):
    menor = min(fat["faturamento"] for fat in fat_diario[mes])
    return menor

def maior_valor(mes):
    maior = max(fat["faturamento"] for fat in fat_diario[mes])
    return maior

def acima_da_media(mes):
    total = sum(fat["faturamento"] for fat in fat_diario[mes])
    dias_faturamento = len(fat_diario["Janeiro"])
    media_faturamento = total / dias_faturamento
    dias_acima = 0
    for dias in fat_diario[mes]:
        if dias["faturamento"] > media_faturamento:
            dias_acima += 1
    return dias_acima



print(f"O menor valor de faturamento no mês de Janeiro foi R${menor_valor('Janeiro')}")
print(f"O maior valor de faturamento no mês de Janeiro foi R${maior_valor('Janeiro')}")
print(f"O mês de janeiro teve {acima_da_media("Janeiro")} dias de faturamento acima da média.")
