import pygame
from random import choice, randint
from pygame.locals import *
from couleur import *

pygame.init()

# classes
from SnakeSprite import SnakeSprite
from Bonbon import Bonbon, GrosBonbon, BonBonbon, TempsBonbon, RetreciBonbon
from CheckCollide import CheckCollide
from Map import Map
from Texte import Texte
from Tools import Tools
from Temps import Temps

class Game:
	def __init__(self, ss, cc, tx, to, tp, mp, bonbon, bonBonbon, grosBonbon, \
		tempsBonbon, retreciBonbon):
		self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
		self.ss = ss()
		self.cc = cc()
		self.tx = tx()
		self.to = to()
		self.tp = tp()
		self.mp = mp()
		self.bonbon        = bonbon
		self.bonBonbon     = bonBo
		self.grosBonbon    = grosBonbon
		self.tempsBonbon   = tempsBonbon
		self.retreciBonbon = retreciBonbon

	def _load_niveau_bonbon(self, nbBonbon, name):
		bonbon = []
		for i in range(nbBonbon):
			bonbon.append(name())
		return bonbon

	def _load_niveau(self, niveau):
		""" Cette fonction sert juste a obtenire self.listeBonbon """
		parametre = niveau[0]
		bonbons   = niveau[1]

		self.tempsJeu          = parametre[0]
		self.tailleQueueDepart = parametre[1]

		bonbon        = self._load_niveau_bonbon(bonbons[0], self.bonbon)
		grosBonbon    = self._load_niveau_bonbon(bonbons[1], self.grosBonbon)
		bonBonbon     = self._load_niveau_bonbon(bonbons[2], self.bonBonbon)
		tempsBonbon   = self._load_niveau_bonbon(bonbons[3], self.tempsBonbon)
		retreciBonbon = self._load_niveau_bonbon(bonbons[0], self.retreciBonbon)

		self.listeBonbon = bonbon + grosBonbon + bonBonbon + \
		tempsBonbon + retreciBonbon

	def _choisi_bonbon(self, liste):
		""" Cette fonction choisi un bonbon dans liste en le retirant """
		LL = len(liste)
		if LL > 0:
			index = randint(0, LL - 1)
			bonbon = liste.pop(index)
		else:
			bonbon = None
		return bonbon, liste

	def play_demo(self):
		niveaux = self.mp.get_demo()
		nbNiveauEnCours = 5
		self._load_niveau(niveaux[nbNiveauEnCours]) # on load le niveau
		# _load_niveau a creer self.listeBonbon
		bonbon, self.listeBonbon = self._choisi_bonbon(self.listeBonbon)

		cont = True
		while cont:
			for e in pygame.event.get():
				if e.type == QUIT:
					cont = False

				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						cont = False



if __name__ == '__main__':
	g = Game(Bonbon, CheckCollide, Texte, Tools, Temps, Map)
	mp = Map()
	g.play_demo()
	print g.listeBonbon
