# --- DESAFIO 013
# --- Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com um aumento de X%.

print('Vamos calcular o aumento salarial!')

funcionario = input('Digite o nome do funcionário: ')
salario_atual = float(input('Digite o valor do salario atual: '))
aumento = int(input('Digite a porcentagem do aumento: '))

aumento_corrigido = salario_atual * (aumento / 100) # --- conta para achar o valor a ser aumentado
novo_salario = salario_atual + aumento_corrigido

print(f'O funcioário {funcionario}, recebera um aumento de {aumento}%! \nE seu novo salario passa a ser R${novo_salario:_.2f}'.replace('_','.'))

print('Vamos considerar o P.P.R.!')

ppr_porc = float(input('Digite a porcentagem do P.P.R.: '))
ppr_calculo = novo_salario * (ppr_porc / 100) # --- conta para achar o valor do PPR

print(f'O valor do seu P.P.R. é de: R${ppr_calculo:_.2f}'.replace('_','.'))

soma = novo_salario + ppr_calculo
print(f'A soma de seu novo salario + seu P.P.R. é de: R${soma:_.2f}'.replace('_','.'))