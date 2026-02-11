# --- DESAFIO 012
# --- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Vamos calcular as pormoções dos produtos!')

produto = float(input('Qual o valor atual do produto: '))
desconto = produto * (5 / 100)
novo_preco = produto - desconto

print(f'Esse produto esta com uma promoção de R${desconto:.2f}! \n Seu preço promocional é de: R${novo_preco:.2f}')