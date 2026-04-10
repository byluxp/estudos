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
print(f'Você digitou {len(valores)} números') # qtd de números digitado
valores.sort(reverse=True) # ordena a lista em ordem decrescente
print(f'Os números em ordem decrescente são: {valores}') # imprime os números digitados em ordem decrescente    
if 5 in valores: # se o número 5 estiver na lista
    print('O número 5 faz parte da lista!') # imprime a mensagem de que o número 5 faz parte da lista
else:    print('O número 5 não faz parte da lista!') # imprime a mensagem de que o número 5 não faz parte da lista