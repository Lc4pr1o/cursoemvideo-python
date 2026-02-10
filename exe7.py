# --- DESAFIO 007
# --- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

aluno = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a 1° Nota: '))
nota2 = int(input('Digite a 2° Nota: '))
soma = nota1 + nota2
media = soma/2

print(f'O aluno {aluno} \nEstá com uma média de: {media}')