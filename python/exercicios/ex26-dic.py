import random
from time import sleep
from operator import itemgetter

jogadores = {}

for j in range(0,6):
    jogada = random.randint(1,6)
    jogadores[f'Jogador {j+1}'] = jogada
for jogador, jogada in jogadores.items():
    print(f'{jogador} tirou {jogada}')
    sleep(1) #faz esperar 1 segundo antes de exibir o proximo

ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # ordena os jogadores com base na jogada, do maior para o menor
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}') # exibe o ranking dos jogadores, onde v[0] é o nome do jogador e v[1] é a jogada. O i+1 é para não começar em 0
    sleep(1) #faz esperar 1 segundo antes de exibir o proximo