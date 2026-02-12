'''
--- RESUMO DA BIBLIOTECA MATH (MATEMÁTICA) ---
Para usar, lembre-se de colocar "import math" na linha 1 do código.

PRINCIPAIS FUNÇÕES:

1. ARREDONDAMENTO
   math.ceil(x)   -> Teto (Ceiling). Arredonda para CIMA.
                     Ex: math.ceil(4.2) vira 5 (Útil para comprar latas de tinta).

   math.floor(x)  -> Chão (Floor). Arredonda para BAIXO.
                     Ex: math.floor(4.9) vira 4.

   math.trunc(x)  -> Truncar. Corta a parte decimal, joga fora a vírgula.
                     Ex: math.trunc(4.9) vira 4 (Sem arredondar).

2. CONTAS
   math.pow(x, y) -> Potência. Faz x elevado a y.
                     Ex: math.pow(5, 2) vira 25.0 (Sempre retorna Float).

   math.sqrt(x)   -> Raiz Quadrada (Square Root).
                     Ex: math.sqrt(81) vira 9.0.

   math.factorial(x) -> Fatorial.
                        Ex: math.factorial(5) vira 120 (5x4x3x2x1).

3. CONSTANTES
   math.pi        -> O valor de Pi (3.14159...).
'''

# Exemplo de uso prático:
import math

num = float(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é {math.ceil(raiz)} (Arredondado para cima)')