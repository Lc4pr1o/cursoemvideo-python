# --- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.
# --- DESAFIO 017

import math

co = float(input('Qual é o comprimento do Cateto Oposto: '))
ca = float(input('Qual é o comprimento do Cateto Adjacente: '))

print(f'Considerando um Cateto Oposto {co}\n E um Cateto Adjacente {co}\n A Hipotenusa é: >>> {math.hypot(co, ca):.2f} <<<')