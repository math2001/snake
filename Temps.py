import pygame
import time
from pygame.locals import *
from couleur import *

class Temps:
	def __init__(self):
		self.timeDebut = 0
		self.timeGame  = 0
		self.timeInit  = False

	def init(self, temps_debut):
		self.timeDebut = time.time() + temps_debut
		self.timeInit = True

	def initForAffichage(self, temps_debut):
		""" cette fonction initialise le temps UNIQUEMENT pour l afficher. La classes considerera pas que le temps sera initialise. Le temps ne cecoulera donc pas """
		self.init(temps_debut)
		self.timeInit = False
		self.timeGame = int(self.timeDebut - time.time())

	def enregistre(self):
		self.timeGame = int(self.timeDebut - time.time())

	def get(self, decimal=None):
		if decimal is None:
			return int(self.timeGame)
		else:
			return round(self.timeGame, decimal)

	def ajoute(self, temps):
		self.timeDebut += temps

	def getInit(self):
		return self.timeInit

	def quit(self):
		self.timeInit = False