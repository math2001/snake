import pygame
from pygame.locals import *
from couleur import *

class Tools:
	def __init__(self):
		pass

	def waitForKeydown(self):
		""" Cette fonction boucle tant que j utilisateur n a pas presse une touche """
		cont = True
		while cont:
			ev = pygame.event.wait()
			if ev.type == KEYDOWN:
				cont = False

	def arr(self, nb, div):
		""" arrondi nb en un multiple de div """
		distance = nb % div
		if distance >= 5:
			return nb + (div - distance)
		else:
			return nb - distance