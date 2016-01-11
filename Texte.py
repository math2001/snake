import pygame
from pygame.locals import *
from couleur import *
from Screen import Screen

class Texte(Screen):
	def __init__(self):
		Screen.__init__(self)
		self.size = 50
		self.font = pygame.font.Font('font/consolas.ttf', self.size)

	def center(self, texte, yajout=0, xajout=0):
		surface = self.font.render(str(texte), False, noir)
		return surface.get_rect(centerx=self.sWidth / 2 + xajout, centery=self.sHeight / 2 + yajout)
	def centerx(self, texte, xajout=0):
		surface = self.font.render(str(texte), False, noir)
		w = surface.get_width()
		return self.sWidth / 2 - w / 2

	def bottom(self, texte):
		surface = self.font.render(str(texte), False, noir)
		h = surface.get_height()
		return self.sHeight - h

	def UTPC(self):
		""" Cette fonction affiche "une touche pour continuer" """
		texte = 'Une touche pour continuer...'
		position = self.centerx(texte), self.bottom(texte)
		texte = self.font.render(texte, True, gris)
		self.screen.blit(texte, position)

	def affiche(self, message, pos=(0, 0), fg=noir, bg=None, center=False, titre=['', red], UTPC=True):
		""" 
			texte doit etre un tuple ou liste 
			pour inserer un retour a la ligne, il suffit juste d inserer un \n
			ex: ('Exemple n ', 8, '\n', 'de retour a la ligne\n', 'tout seul ou accompagne \n', '\n')
		"""
		texteTransform = ''
		# cette boucle sert a ne pas s embeter a transformer les int en str quand on appelle la fonction
		for el in message:
			texteTransform += str(el)

		self.font.set_underline(True)
		titreR = self.font.render(titre[0], True, titre[1])
		self.font.set_underline(False)

		self.screen.blit(titreR, (self.centerx(titre[0]), 50))
		texteTransform = texteTransform.split('\n')
		pos = list(pos)
		yajout = pos[1] - 25 * len(texteTransform)
		for ligne in texteTransform:
			if bg is not None:
				message = self.font.render(ligne, True, fg, bg)
			else:
				message = self.font.render(ligne, True, fg)
			if center:
				pos = list(self.center(ligne, yajout=yajout))
				yajout += 50
			self.screen.blit(message, pos)
			pos[1] += 50
		if UTPC:
			self.UTPC()

	def affiche2(self, texte, pos=(0, 0), center=False, titre=['', red], UTPC=True):
		""" texte doit etre un tuple.
			Faites une liste avec le texte et la couleur. Entre chaque liste, il y
			aura un retour la la ligne
			Plan :
			[texte, fg, bg], [texte, fg, bg], ...
			texte doit etre une liste
			Exemple :
			[['un texte en rouge avec fond noir', un_chiffre], rouge, noir], 
			[['un texte en bleu sans fond'], bleu, None],
			[[score], noir, None]
		"""

		self.font.set_underline(True)
		titreR = self.font.render(titre[0], True, titre[1])
		self.font.set_underline(False)
		self.screen.blit(titreR, (self.centerx(titre[0]), 50))

		pos = list(pos)
		yajout = pos[1] - 25 * len(texte)
		for caracteristique in texte:
			# cette boucle sert a ne pas s embeter a transformer les int en str
			# quand on appelle la fonction
			strElementTexte = ''
			for elementTexte in caracteristique[0]:
				strElementTexte += str(elementTexte)
				

			if caracteristique[2] is None: 
				texteRender = self.font.render(strElementTexte, True, caracteristique[1])
			else:
				texteRender = self.font.render(strElementTexte, True, caracteristique[1], caracteristique[2])

			if center:
				pos = list(self.center(caracteristique[0], yajout=yajout))
				yajout += 50
			self.screen.blit(texteRender, pos)
			pos[1] += 50

		if UTPC:
			self.UTPC()	