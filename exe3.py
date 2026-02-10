
#---DESAFIO003
    #---Crie um programa que leia dois numeros e mostre a soma entre eles
n1 = int(input('Me passa o Primeiro numero que você quer somar? '))
n2 = int(input('Me passa o Segundo numero que você quer somar? '))

soma = n1 + n2

print(f'\nA soma entre {n1} e {n2} \nresulta em: {soma}!')


# f é um recurso mais moderno do Python (chamado de f-string) que serve para avisar o computador:
# "Ei Python, dentro dessas aspas não tem apenas texto comum. Tem variáveis que você precisa trocar pelos valores reais!"
