def affiche(texte, pos=(0, 0), center=False, titre=['', 'red'], UTPC=True):
	""" texte doit etre un tuple.
		Faites une liste avec le texte et la couleur. Entre chaque liste, il y
		aura un retour la la ligne
		Plan :
		[texte, fg, bg], [texte, fg, bg], ...
		texte doit etre une liste
		Exemple :
		[['un texte en rouge avec fond noir', un_chiffre], 'rouge', 'noir'], 
		[['un texte en bleu sans fond'], 'bleu', None],
		[[score], 'noir', None]
	"""

	self.font.set_underline(True)
	titreR = self.font.render(titre[0], True, titre[1])
	self.font.set_underline(False)
	self.screen.blit(titreR, (self.centerx(titre[0]), 50))

	yajout = pos[1] - 25 * len(texte)
	for liste in texte:
		# cette boucle sert a ne pas s embeter a transformer les int en str
		# quand on appelle la fonction
		for elementTexte in liste[0]
			elementTexte = str(elementTexte)

		if liste[2] is None: 
			texteRender = self.font.render(elementTexte, True, liste[1])
		else:
			texteRender = self.font.render(elementTexte, True, liste[1], liste[2])

		if center:
			pos = list(self.center(ligne, yajout=yajout))
			yajout += 50
		self.screen.blit(message, pos)
		pos[1] += 50
		if UTPC:
			self.UTPC()	