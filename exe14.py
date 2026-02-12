# --- DESAFIO 014
# --- Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite o a temperatura a ser convertida: '))

f = (c * 1.8) + 32 # --- Essa é a formula fixa para converter celsius em fahrenheit.

print(f'Vamos converter {c:.1f}°C em em fahrenheit! \n{c:.1f}°C em fahrenheit é quivalente a {f:.1f}°F ')