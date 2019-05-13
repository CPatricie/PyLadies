import random

def tah_pocitace(pole):
    while True:
        misto = random.randint(0, 19)
        if "-" == pole[pozice]:
            pole = tah(pole, pozice, "o")
            return pole


def tah(pole, pozice, symbol):
    pole = pole[:pozice] + symbol + pole[pozice+1:]
    return pole
