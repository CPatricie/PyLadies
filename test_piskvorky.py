from piskvorky import vyhodnot
from ai import tah_pocitace, tah
import pytest


def test_vyhodnot():
	assert vyhodnot("xxx") == "x", 'Vyhrála jsi!'
	assert vyhodnot("ooo") == "o", 'Vyhrál počítač!'
	assert vyhodnot("xoxooxoxxoxoxooxoxxo") == "!", 'Remíza!'
	assert vyhodnot("xoxooxox--xox--xooxo") == "-", "Hra ještě neskončila!"
	
def test_vyhodnot2():
	pole = 20* "-"
	if vyhodnot(pole) != "-":
		raise Exception("Ve vyhodnocování vítězství hráče nastala chyba")


def test_tah():
	assert tah(pole = 20* "-", pozice = 5, symbol = "x") == "-----x--------------"
	assert tah(pole = 20* "-", pozice = 13, symbol = "x") == "-------------x------"

def test_tah_pocitace():
	pole = tah_pocitace(pole = "-"*20)
	if pole.count("o") != 1:
		raise Exception("Tah se zaznamenal jinak-krát než jednou")
	if "o" not in pole:
		raise Exception("Tah se nezaznamenal.")

# python -m pytest -v test_piskvorky.py