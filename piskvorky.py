"""
Rozděl 1D Piškvorky na čtyři moduly:

ai.py, kde bude funkce tah_pocitace,
piskvorky.py, kde budou ostatní funkce,
hra.py, kde bude import a volání hlavní funkce z piskvorky.py (a nic jiného),
test_piskvorky.py, kde budou testy.
Jak se do importů nezamotat? Podívej se do materiálů na sekci cyklické importy.

Pokud jsi byla na workshopu Gitu, dej to do Gitu! A kdybys něco nedopatřením 
rozbila, git diff HEAD ukáže změny od poslední revize.
"""


import ai

def vyhodnot(pole):
    if "x"*3 in pole:
        return "x"
    elif "o"*3 in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah_hrace(pole):
	while True:
		pozice = input(f"Zadej číslo pozice, na kterou chceš hrát: ")
		if pozice.isdigit():
			pozice = int(pozice)
			if pozice in range(len(pole)):
				if "-" == pole[pozice]:
					pole = ai.tah(pole, pozice, "x")
					return pole
				else:
					print("Pozice je již obsazena!")
			else:
				print("Číslo pozice musí být v rozmezí 0 až ", len(pole) - 1)
		else:
			print("Zadala jsi písmeno anebo záporné číslo.")



def piskvorky1d():
	pole = 20 * "-"
	while True:
		print(pole)
		pole = tah_hrace(pole)
		print(pole)
		if vyhodnot(pole) != "-":
			break
		pole = ai.tah_pocitace(pole)
		if vyhodnot(pole) != "-":
			break

	print(pole)
	if vyhodnot(pole) == "!":
		print('Remíza!')
	elif vyhodnot(pole) == "x":
		print('Vyhrála jsi!')
	elif vyhodnot(pole) == "o":
		print('Vyhrál počítač!')
