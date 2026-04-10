matriz = [[], [], []]
x = 0

for i in range (0,3):
    for j in range (0,3):
        pos = int(input(f'Digite o valor para:[{i}][{j}] ')) #o i inicia em 0 e o j que aumenta. no for não precisa coloca i += i
        matriz[i].append(pos) # a matriz vira o valor de i e muda quando i mudar

for i in range(0,3):
        for j in range(0,3):
            print(f'[{matriz[i][j]}]',end='') #lembrar de usar o f | o end evita de pular linha automaticamente antes de acabar o loop do j
        print() #lembrar de identar bem