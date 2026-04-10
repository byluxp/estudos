lista = [] 
maior = menor = 0

for c in range(0,5):
    n = (int(input('Digite um número: '))) # pede para o usuário digitar um número
    if c == 0 or n > (lista[-1]):  # se for o primeiro número digitado (c indica a posição) ou se for maior que o ultimo valor
        lista.append(n) # adiciona o número à lista
    else:
        pos = 0 # inicia a posição como 0
        while pos < len(lista): # enquanto posição por < que o tamanho da lista
            if n <= lista[pos]: # se o numero for <= a posição atual que está sendo verificada
                lista.insert(pos, n) # insere o número na posição atual (o numero da posição atual vira o proximo da lista)
                print(f'Numero adicionado na posição {pos} da lista') # imprime a mensagem de sucesso com a posição do número adicionado
                break # sai do loop
            pos += 1 # caso contrário, acrescenta +1 na posição para verificar a proxima posição  
print(f'Os números digitados são: {lista}') # imprime os números digitados em ordem crescente