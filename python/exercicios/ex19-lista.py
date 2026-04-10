valores = [] # cria uma lista vazia para armazenar os números digitados pelo usuário
par = [] # cria uma lista vazia para armazenar os números pares digitados pelo usuário
impar = [] # cria uma lista vazia para armazenar os números ímpares digit

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    if n % 2 == 0 and n not in par:
        par.append(n)
        print('Número par adicionado com sucesso!')
    elif n % 2 != 0 and n not in impar:
        impar.append(n)
        print('Número ímpar adicionado com sucesso!')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Você digitou os números: {valores}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')