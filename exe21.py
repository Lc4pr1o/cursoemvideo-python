# --- Faça um programa em python que abra e reproduza um audio de um arquivo MP3.
# --- DESAFIO 021

import pygame

# 1. Iniciar a biblioteca (Ligar o motor do carro)
pygame.init() 

# 2. Carregar o arquivo de som (Colocar o CD no player)
# Substitua 'musica.mp3' pelo nome exato do seu arquivo
pygame.mixer.music.load('musica.mp3')

# 3. Dar o Play (Apertar o botão de tocar)
pygame.mixer.music.play()

# 4. O SEGREDO (O Freio de Mão)
# Sem isso, o Python dá o play e encerra o programa no mesmo milésimo de segundo.
# O input segura o programa aberto para você ouvir o som.
input('Curte o som! Aperte Enter para parar...')