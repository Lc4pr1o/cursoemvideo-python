# --- DESAFIO 005
# --- Crie um programa que leia um numeros inteiro e mostre na tela o seu sucessor e antecessor.


pergunta = int(input('Digite um numero: '))
ante = pergunta - 1
suce = pergunta + 1

print(f'O numero digitado: {pergunta} \n seu Sucessor é: {suce}\n seu Antecessor é: {ante}')