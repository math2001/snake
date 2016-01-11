""" 
Il y a une ambiguite entre map et niveau
Une map est un *ensemble* de niveau

TYPE :
1 => Bonbon() 
2 => GrosBonbon()
3 => BonBonbon()
4 => TempsBonbon()
5 => RetreciBonbon()

PLAN D'UNE MAP :

[parametres, bonbon]

parametres = [
	temps_de_jeu, # en sec
	taille_queue_depart
]
bonbon = [            => Map
	nb_bonbon_type1, -
	nb_bonbon_type2,  |
	nb_bonbon_type3,  | => Niveau 
	nb_bonbon_type4,  |
	nb_bonbon_type5  _
] 
"""


import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

class Map(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.mapDemo = [
			[[60, 10], [5, 0, 0, 0, 0]],
			[[30, 10], [0, 2, 0, 0, 0]],
			[[40, 10], [0, 0, 3, 0, 0]],
			[[10, 10], [0, 0, 0, 3, 0]],
			[[20, 30], [0, 0, 0, 0, 4]],

			[[20, 10], [5, 2, 6, 5, 7]] # test	
		]

	def get_demo(self):
		return self.mapDemo