print("Olá, seja bem-vindo à nossa loja.")
print("Compras acima de 200 reais recebem 10% de desconto, e compras acima de 500 reais recebem 20% de desconto.")
compra = float(input("Quanto ficou o valor da compra? R$ "))

if compra >= 500:
    print(f"Você ganhou um desconto de 20% e a compra ficaria no valor de: R${compra - (compra * 0.20):.2f}")
    print(f"Valor original: R${compra:.2f}")
    print(f"Valor com desconto: R${compra - (compra * 0.20):.2f}")
    print("Obrigado por sua compra!")
elif compra >= 200:
    print(f"Você ganhou um desconto de 10% e a compra ficaria no valor de: R${compra - (compra * 0.10):.2f}")
    print(f"Valor original: R${compra:.2f}")
    print(f"Valor com desconto: R${compra - (compra * 0.10):.2f}")
    print("Obrigado por sua compra!")
else:
    print("Obrigado por sua compra!")