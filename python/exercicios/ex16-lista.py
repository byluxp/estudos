n = [] 
maior = menor = 0

for c in range(0,5):
    n.append(int(input('Digite um número: '))) # pede para o usuário digitar um número
    if c == 0: # se c for igual a 0
        maior = menor = n[0] # maior e menor se tornam o número digitado
    else:
        if n[c] > maior: # se o número digitado for maior que o maior
            maior = n[c] # maior se torna o número digitado
        if n[c] < menor: # se o número digitado for menor que o menor
            menor = n[c] # menor se torna o número digitado
print(f'Os numeros digitados foram: {n}') # imprime os números digitados
print(f'O maior número digitado foi: {maior} nas posições {list(enumerate([i for i, x in enumerate(n) if x == maior]))}') # imprime o maior número digitado
print(f'O menor número digitado foi: {menor} nas posições {list(enumerate([i for i, x in enumerate(n) if x == menor]))}') # imprime o menor número digitado