# --- Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# --- DESAFIO 016

import math
num = (float(input('Digite um numero: ')))

print(f'O número {num} tema parte inteira {math.trunc(num)}')