y = 0
for c in range(1,6):
    s = int(input('Digite um valor: '))
    if s % 2 == 0:
       s = 0
    else:
        y += s
    print (y)
print('Soma: ', y)