import pygame
from pygame.locals import *
from couleur import *
class Screen:
	def __init__(self, titre='Snake'):
		self.screen  = pygame.display.get_surface()
		self.sSize   = self.screen.get_size()
		self.sWidth  = self.sSize[0]
		self.sHeight = self.sSize[1]
		pygame.display.set_caption(titre)
