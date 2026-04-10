import random

jogos = int (input('Quantos jogos deseja fazer? ')) # solicita a quantidade de jogos que o usuário deseja fazer
jogo = [] # cria uma lista vazia para armazenar os jogos

for i in range(0, jogos): 
    for j in range(0,6):
        num = random.randint(1,60) # gera um número aleatório entre 1 e 60
        while num in jogo: # verifica se o número já foi gerado para evitar repetições
            num = random.randint(1,60) # gera um novo número se o anterior já foi gerado
        jogo.append(num) # adiciona o número à lista do jogo
    jogo.sort() # ordena os números do jogo
    print(f'Jogo {i+1}: {jogo}') # exibe o jogo. o +1 é para não começar em 0
    jogo.clear() # limpa a lista do jogo para o próximo jogo 
    