'''
--- RESUMO DA BIBLIOTECA RANDOM (ALEATÓRIO) ---
Para usar, lembre-se de colocar "import random" na linha 1 do código.

1. NÚMEROS
   random.randint(a, b) -> Retorna um número INTEIRO aleatório entre a e b.
                           Ex: random.randint(1, 10) pode dar 1, 5, 10...
                           (Útil para jogar dados ou escolher um número secreto).

   random.random()      -> Retorna um número DECIMAL (float) entre 0 e 1.
                           Ex: 0.154, 0.999...
                           (Útil para probabilidades).

   random.uniform(a, b) -> Retorna um número DECIMAL aleatório entre a e b.
                           Ex: random.uniform(1.5, 10.5).

2. LISTAS E SORTEIOS
   random.choice(lista) -> Escolhe UM item aleatório da lista.
                           Ex: lista = ['Ana', 'Beto', 'Carla']
                               sorteado = random.choice(lista)

   random.shuffle(lista)-> EMBARALHA a lista original (muda a ordem dela).
                           Ex: random.shuffle(lista)
                           (Útil para embaralhar cartas ou ordem de apresentação).

   random.sample(lista, k) -> Escolhe K itens da lista SEM REPETIR.
                              Ex: random.sample(lista, 2) pega 2 nomes diferentes.
'''

# Exemplo rápido:
import random

aluno = random.choice(['Pedra', 'Papel', 'Tesoura'])
print(f'O computador escolheu: {aluno}')