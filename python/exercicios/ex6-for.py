s = 0
for c in range(1,500):
    if c % 3 == 0 and c % 2 != 0: # se o resto da divisão por 3 for 0 e o número for ímpar
        s += c # s = s + c
print (s)