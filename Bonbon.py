import pygame
from pygame.locals import *
from random import randrange
from couleur import *
from Screen import Screen

class Bonbon(Screen):
	def __init__(self):
		Screen.__init__(self)

		# image
		self.bonbon = pygame.image.load('image/bonbon/bonbon.png').convert_alpha()
		self.rect = self.bonbon.get_rect()
		self.tailleSprite = 15

		# son (quand on le mange)
		self.son = pygame.mixer.Sound('son/ting.wav')

		self.giveQueue = 1 # nombre de sprite de queue rajoute quand on mange le bonbon
		self.giveScore = 2 # nombre de score donne quand on mange le bonbon
		self.giveTemps = 0 # nombre de sconde donne quand on mange le bonbon

	def position(self):
		""" Cette fonction tire une position pour un bonbon au hasard """
		r = randrange
		pos = r(self.tailleSprite, self.sWidth - self.tailleSprite * 2, self.tailleSprite), r(self.tailleSprite, self.sHeight - self.tailleSprite * 2, self.tailleSprite)
		# on remet le rect a (0, 0) pour ne pas qu il sorte de l ecran quand on le replace
		self.rect.x = self.rect.y = 0 
		self.rect = self.rect.move(pos)

	def getRect(self):
		return self.rect

	def getGiveQueue(self):
		return self.giveQueue

	def getGiveScore(self):
		return self.giveScore

	def getGiveTemps(self):
		return self.giveTemps

	def playSound(self):
		self.son.play()

	def affiche(self):
		self.screen.blit(self.bonbon, self.rect)


# --------------------------------------------------------------------------------------------- #
# ---------------------- Bonbons Speciaux - Heritage de la classe Bonbon ---------------------- #
# --------------------------------------------------------------------------------------------- #


class GrosBonbon(Bonbon):
	def __init__(self):
		Bonbon.__init__(self)
		self.bonbon = pygame.image.load('image/bonbon/gros-bonbon.png')
		self.rect = self.bonbon.get_rect()
		self.tailleSprite = 30

		self.son = pygame.mixer.Sound('son/gonfle.wav')

		self.giveQueue = 5
		self.giveScore = 1
		self.giveTemps = 0

class BonBonbon(Bonbon):
	def __init__(self):
		Bonbon.__init__(self)
		self.bonbon = pygame.image.load('image/bonbon/bon-bonbon.png').convert_alpha()
		self.rect = self.bonbon.get_rect()
		self.tailleSprite = 15

		self.son = pygame.mixer.Sound('son/miam.wav') # pas encore valide

		self.giveQueue = 0
		self.giveScore = 3
		self.giveTemps = 0

class TempsBonbon(Bonbon):
	def __init__(self):
		Bonbon.__init__(self)
		self.bonbon = pygame.image.load('image/bonbon/temps-bonbon.png').convert_alpha()
		self.rect = self.bonbon.get_rect()
		self.tailleSprite = 15

		self.son = pygame.mixer.Sound('son/tic-tac.wav') # pas encore valide

		self.giveQueue = 0
		self.giveScore = 1
		self.giveTemps = 10

class RetreciBonbon(Bonbon):
	def __init__(self):
		Bonbon.__init__(self)
		self.bonbon = pygame.image.load('image/bonbon/retreci-bonbon.png').convert_alpha()
		self.rect = self.bonbon.get_rect()
		self.tailleSprite = 15

		self.son = pygame.mixer.Sound('son/aspire.wav')

		self.giveQueue = -5
		self.giveScore = 0
		self.giveTemps = 0