#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Description:
		Calcule récursivement la factorielle d’un nombre entier non négatif.

	Parameters:
		n (int): Nombre entier non négatif dont on veut calculer la factorielle.

	Returns:
		int: La factorielle de n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
