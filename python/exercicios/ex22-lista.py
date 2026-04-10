matriz = [[], [], []]
pares = soma = maior = 0

for i in range (0,3):
    for j in range (0,3):
        pos = int(input(f'Digite o valor para:[{i}][{j}] ')) #o i inicia em 0 e o j que aumenta. no for não precisa coloca i += i
        matriz[i].append(pos) # a matriz vira o valor de i e muda quando i mudar
        if pos % 2 == 0:
            pares += pos
    if j == 2:
     soma +=pos

for i in range(0,3):
    valor_atual = matriz[i][1]
    if i == 0:
        maior = valor_atual
    else:
        if valor_atual > maior:
            maior = valor_atual


for i in range(0,3):
        for j in range(0,3):
            print(f'[{matriz[i][j]}]',end='') #lembrar de usar o f | o end evita de pular linha automaticamente antes de acabar o loop do j
        print() #lembrar de identar bem

print(f'A soma dos valores é: {pares}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda coluna é: {maior}')