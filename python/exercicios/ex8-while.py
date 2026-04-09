import random
compt = random.randint(1,10) # gera um número aleatório entre 1 e 10
jogadas = 0
jogador = 0

while jogador != compt: # enquanto o jogador não acertar o número
    jogador = int(input('Digite um número entre 1 e 10: ')) # pede para o jogador digitar um número
    jogadas += 1 # incrementa o número de jogadas
print('Parabéns! Você acertou o número em', jogadas, 'jogadas. O numero era {}'.format(compt)) # imprime a mensagem de parabéns e o número de jogadas
    