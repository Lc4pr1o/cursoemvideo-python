# --- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# --- DESAFIO 18

import math

ang = float(input('Digite o angulo: '))

ang_conv = math.radians(ang)

seno = math.sin(ang_conv)
cos = math.cos(ang_conv)
tan = math.tan(ang_conv)

print(f'Ângulo digitado: > {ang} <\n - Seno: {seno:.2f}\n - Cosseno: {cos:.2f}\n - Tangente: {tan:.2f}')