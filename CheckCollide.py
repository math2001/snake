import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

class CheckCollide(Screen):
	def __init__(self):
		Screen.__init__(self)

	def withLolly(self, teteRect, bonbonRect):
		if teteRect.colliderect(bonbonRect):
			return True
		else:
			return False

	def withQueue(self, teteRect, queue):
		""" queue doit etre la liste de chaque position des sprites des queues """
		# collidelist retourne -1 quand teteRect ne touche rien dans la liste
		if teteRect.collidelist(queue) != -1:
			# si touts les sprites de la queue sont sur la meme case que la tete,
			# c est que le jeu vien de (re)demarrer, donc il ne faut pas retourner True
			for ke in queue:
				if (ke.x, ke.y) == (teteRect.x, teteRect.y):
					restartJeu = True
				else:
					restartJeu = False
			if not restartJeu:
				return True
			else:
				return False
			return True
		else:
			return False