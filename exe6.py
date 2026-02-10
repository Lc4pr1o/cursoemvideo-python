# --- DESAFIO 006
# --- Crie um algoritmo que leia um numero e mostre o seu dorbo, Triplo e raiz quadrada.

pergunta = int(input('Digite um numero: '))

dobro = pergunta * 2
triplo = pergunta * 3
raiz = pergunta ** 0.5

"""
Raiz Quadrada = Elevar a 1/2 (ou 0.5)
Raiz Cúbica = Elevar a 1/3 (ou 0.333)
Raiz Quarta = Elevar a 1/4 (ou 0.25)
"""

print(f'O numero digitado foi: {pergunta} \n sendo que; \n Seu Dobro é: {dobro} \n Seu Triblo é: {triplo} \n Sua Raiz Quadrada é: {raiz:0.3}')