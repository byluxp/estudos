valores = [] # cria uma lista vazia para armazenar os números digitados pelo usuário

while True:
    n = int(input('Digite um número: ')) # pede para o usuário digitar um número
    if n not in valores: # se o número digitado não estiver na lista
        valores.append(n) # adiciona o número à lista
        print('Número adicionado com sucesso!') # imprime a mensagem de sucesso
    else:
        print('Número duplicado!') # imprime a mensagem de número duplicado
    resp = str(input('Quer continuar? [S/N] ')).strip().upper() # pergunta se o usuário quer continuar
    if resp == 'N': # se a resposta for N
        break # sai do loop

valores.sort() # ordena a lista em ordem crescente

print(f'Você digitou os números: {valores}') # imprime os números digitados