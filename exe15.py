# --- DESAFIO 015
# --- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Vamos calcular o seu custo de viagem com aluguel de carro!')

km = float(input('Quantos KM foram percorridos: '))
dias = int(input('Quantos dias de aluguel do carro: '))

print(f'Considerando que cada dia de alguel custa R$60,00 \nE existe uma taxa de R$0,15 por KM percorrido.')

aluguel = dias * 60
taxa = km * 0.15

print(f'Seu custo de viagem foi de R${aluguel:.2f}, com alguel do carro!\n E R${taxa:.2f} com taxas!')
print(f'Totalizando um gasto de R${aluguel + taxa:.2f}')