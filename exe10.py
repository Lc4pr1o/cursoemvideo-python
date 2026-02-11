# --- DESAFIO 010
# --- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# --- Cotação atual do dolar 10/02/2026 {5,20}

carteira = float(input('Informe seu saldo atual: '))
dolar = 5.20
trade = carteira / dolar

print('Cotação atual do Dolar: $1.00 = R$5.20')

print(f'Com o seu saldo atual é possivel comprar: ${trade:_.2f}'.replace('_','.'))

