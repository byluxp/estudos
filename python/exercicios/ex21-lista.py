lista = [[], []] # cria uma lista com duas sublistas vazias para armazenar os números pares e ímpares digitados pelo usuário

for x in range(0, 6):
    n = int(input('Digite um número: ')) ## solicita numero n
    if n % 2 == 0:## verifica se é par
        lista[0].append(n) # adiciona na lista posição 0
    else:            
        lista[1].append(n) # adiciona na lista posição 1

lista[0].sort()
lista[1].sort()
print(f'Os números digitados foram: {lista}')

