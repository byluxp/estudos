from random import randint
from time import sleep

listaSorteio = []

def sorteio():
    global listaSorteio
    listaSorteio = []
    for i in range(0,5):
        randNum = randint(1,10)
        print(randNum, end=' ')
        listaSorteio.append(randNum)
        sleep(0.3)
    print('PRONTO!')

def somaPar():
    somaPar = 0
    for v in (listaSorteio):
        if v % 2 == 0:
            somaPar += v
    print(f'Soma dos números pares: {somaPar}')


sorteio()
sleep(1)
somaPar()