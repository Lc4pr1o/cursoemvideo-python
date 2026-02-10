# --- DESAFIO 008
# --- Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetro.

entrada = int(input('Digite o valor a ser convertido: '))
cm = entrada * 100
mm = entrada * 1000


# --- TRUQUE DE FORMATAÇÃO (Padrão BR) ---
# O Python usa vírgula ou underline para separar milhar (padrão americano).
# Para ficar com ponto (padrão Brasil: 1.000), usamos essa lógica:
# 1. O ":_" dentro das chaves formata com underline (ex: 20_000)
# 2. O ".replace" troca todos os underlines por pontos (ex: 20.000)

#print(f'A medida é {mm:_}mm'.replace('_', '.'))

print(f'Valor digitado foi: {entrada} metros\nConvertendo em Centimetros temos: {cm:_}cm\nConvertendo em Milimetros temos: {mm:_}mm'.replace('_', '.'))