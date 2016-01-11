import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen
from Tools import Tools

tl = Tools()

def NoneFonction():
	pass
class SnakeSprite(Screen):
	def __init__(self):
		self.snake    = pygame.image.load('image/snake/snake_sprite_tete.png').convert_alpha()
		self.imgQueue = pygame.image.load('image/snake/snake_sprite_queue.png')
		self.rect     = self.snake.get_rect()
		# le jeu est fait en sprit. Il font 15px de cote. Le serpent se deplace donc de sprite en sprite, donc de sa taille [de sprite] par sa taille, donc de 15px
		self.vitesse  = self.snake.get_width()
		self.speed    = [0, 0]

		self.gameLost = False
		Screen.__init__(self)

		x, y = self.sWidth / 2, self.sHeight / 2
		x, y = tl.arr(x, self.vitesse), tl.arr(y, self.vitesse)
		self.posDefaut = x, y
		self.rect = self.rect.move(self.posDefaut)

		self.queue = []
		self.nbSpriteQueueDefaut = 50
		self.nbSpriteQueue = self.nbSpriteQueueDefaut

		self.score = 0

	def changeDir(self, kgp):
		# x move
		if kgp[K_LEFT] and self.speed[0] == 0:
			self.speed = -self.vitesse, 0

		elif kgp[K_RIGHT] and self.speed[0] == 0:
			self.speed = self.vitesse, 0

		# y move

		elif kgp[K_UP] and self.speed[1] == 0:
			self.speed = 0, -self.vitesse
		
		elif kgp[K_DOWN] and self.speed[1] == 0:
			self.speed = 0, self.vitesse

		if self.speed == [0, 0]:
			return False # l utilisateur n a pas encore presse de touche
		else:
			return True # l utilisateur a presse une touche

	def move(self):
		if self.rect.left <= 0 or self.rect.right >= self.sWidth \
		or self.rect.top <= 0 or self.rect.bottom >= self.sHeight:
			self.speed = 0, 0
			return False
		else:
			self.rect = self.rect.move(self.speed)
			return True

	def enregistreQueue(self):
		self.queue.append(self.rect)
		# on supprime la queue en trop
		while len(self.queue) > self.nbSpriteQueue:
			del(self.queue[0])

	def reset(self):
		""" Cette fonction remet le serpent comme il ete a la base """
		self.nbSpriteQueue = self.nbSpriteQueueDefaut
		self.score = 0
		self.rect.x = 0
		self.rect.y = 0
		self.rect = self.rect.move(self.posDefaut)
		self.queue = [] # desactive ca, ca fait un truc marrant (mais pas logique, c est pour ca que je l ai mis)
		self.speed = [0, 0]

	def getQueue(self):
		""" retourne la liste des positions de chaque sprite de la queue """
		return self.queue

	def getNbQueue(self):
		""" retourne le nombre de sprite de queue """
		return len(self.queue)

	def ajoutLongueurQueue(self, ajout):
		""" ajout peut etre negatif """
		self.nbSpriteQueue += ajout
		if self.nbSpriteQueue <= 0:
			self.nbSpriteQueue = 0

	def ajoutScore(self, score):
		""" score peut etre negatif """
		self.score += score

	def getTete(self):
		""" retourne le rect de la tete du serpent """
		return self.rect

	def getScore(self):
		""" retourne le score du joueur """
		return self.score

	def setSpriteQueueDefaut(self, value):
		try:
			value = int(value)
		except:
			print 'Value doit etre un int !'
			value = 10
		self.nbSpriteQueueDefaut = value
		self.nbSpriteQueue = self.nbSpriteQueueDefaut

	def affiche(self):
		for spriteQueue in self.queue:
			self.screen.blit(self.imgQueue, spriteQueue)
		self.screen.blit(self.snake, self.rect)
