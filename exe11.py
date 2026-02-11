# --- DESAFIO 011
# --- Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m(ao quadrado)

print('Vamos calcular o quanto de tinta precisamos comprar!')

altura = float(input('Qual a altura exata da sua parede?: '))
largura = float(input('E agora qual a largura exata da sua parede?: '))
area = altura * largura
quantidade = area / 2
latas = int(quantidade + 0.99) # --- Como nainda ão aprendi sobre Bibliotecas/outros operadores, foi a unica forma que encontrei pra arredondar o resultado.

print(f'Considerando que a lata de tinta rende 2m(quadrados) por L \ne temos uma área total de {area:.2f}m \nvamos precisar de {latas} latas de tinta!')