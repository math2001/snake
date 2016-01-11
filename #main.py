# modules
import pygame
import time
from random import choice
from pygame.locals import *
from couleur import *



# classes
from SnakeSprite import SnakeSprite
from Bonbon import Bonbon, GrosBonbon, BonBonbon, TempsBonbon, RetreciBonbon
from CheckCollide import CheckCollide
from Texte import Texte
from Tools import Tools
from Temps import Temps

pygame.init()

mf = pygame.display.set_mode((0, 0), FULLSCREEN)


# -------------------------------------------------------------------------------------------- #
# ----------------------------------- Variables a modifier ----------------------------------- #
# -------------------------------------------------------------------------------------------- #

# plus DELAY est grand, plus le jeu est lent
DELAY = 100

# plus DELAY_MIN_MESSAGE est grand, plus le minimum 
# de temps a attendre lorsqu un message s affiche est long
DELAY_MIN_MESSAGE = 1000

# temps qu'on a au debut
TEMPS_DEBUT = 50 # en sec

# La liste des types de bonbon.
listeTypeBonbon = [Bonbon(), GrosBonbon(), BonBonbon(), TempsBonbon(), RetreciBonbon()]

TAILLE_QUEUE_DEFAUT = 10

# -------------------------------------------------------------------------------------------- #
# ------------------------------- Fin des variables a modifier ------------------------------- #
# -------------------------------------------------------------------------------------------- #

TEMPS_DEBUT += 1

# class init
ss = SnakeSprite()
bb = Bonbon()
cc = CheckCollide()
tt = Texte()
to = Tools()
tp = Temps()

ss.setSpriteQueueDefaut(TAILLE_QUEUE_DEFAUT)

# on tire une position au hasard pour le bonbon (C est forcement un bonbon normal)
bb.position() 

# on desactive l affichage de la souris
pygame.mouse.set_visible(False)
cont = True
clock = pygame.time.Clock()
tp.initForAffichage(TEMPS_DEBUT)
while cont:
	mf.fill(blanc)

	if tp.getInit() and tp.getInit():
		tp.enregistre()

	for e in pygame.event.get():
		if e.type == QUIT:
			cont = False

		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				cont = False

			if e.key == K_SPACE:
				bb = choice(listeTypeBonbon)
				bb.position()

	# on recupere les touches pressees
	kgp = pygame.key.get_pressed()

	# on change la direction du serpent
	if not ss.changeDir(kgp):
		tp.init(TEMPS_DEBUT)

	# ----------------------------------------------------------------------------------------- #
	# --------------- on verifie que la tete du serpent ne touche pas un bonbon --------------- #
	# ----------------------------------------------------------------------------------------- #
	
	if cc.withLolly(ss.getTete(), bb.getRect()):
		# on agrandie le serpent
		ss.ajoutLongueurQueue(bb.getGiveQueue()) 
		# on ajoute du score au serpent
		ss.ajoutScore(bb.getGiveScore())

		# on ajoute du temps
		tp.ajoute(bb.getGiveTemps())

		# on joue le son quand on mange ce bonbon
		bb.playSound() 
		# on tire un type de balle
		bb = choice(listeTypeBonbon)
		# on retire une position [du bonbon] au hasard
		bb.position()

	# ------------------------------------------------------------------------------------------ #
	# ---------------- on verifie que la tete du serpent ne touche pas sa queue ---------------- #
	# ------------------------------------------------------------------------------------------ #
	
	if cc.withQueue(ss.getTete(), ss.getQueue()):
		mf.fill(-1)
		texte2 = (
				['Vous ne devez pas manger votre queue, voyons !', noir, None],
				[('Votre score est de : ', ss.getScore()), noir, None]
			)
		tt.affiche2(texte2, center=True, titre=['Game Over !', red])
		pygame.display.flip()
		pygame.time.delay(DELAY_MIN_MESSAGE)
		# on retire tout les event KEYDOWN de la queue
		pygame.event.clear(KEYDOWN)
		to.waitForKeydown()
		ss.reset()
		tp.init(TEMPS_DEBUT)

	tpget = tp.get()
	if tpget <= 30:
		mf.fill((63, 72, 204))
		if tpget % 5 == 0:
			mf.fill(blanc)

	# on enregistre la queue du serpent
	ss.enregistreQueue()

	# on affiche le serpent (en entier)
	ss.affiche() 

	# on affiche le bonbon
	bb.affiche()

	# ---------------------------------------------------------------------------------------- #
	# ----------------------------------- Statut du joueur ----------------------------------- #
	# ---------------------------------------------------------------------------------------- #
	couleurScore = gris
	couleurTemps = gris
	couleurQueue = gris
	if tp.get() <= 10:
		couleurTemps = rouge
	texte = (
			[['Score : ', ss.getScore()], couleurScore, None], 
			[['Temps : ', tp.get()], couleurTemps, None],
			[['Queue : ', ss.getNbQueue()], couleurQueue, None]
		)
	tt.affiche2(texte, UTPC=False, pos=(5, 5))
	
	# ----------------------------------------------------------------------------------------- #
	# ---------------------------- On verifie qu il reste du temps ---------------------------- #
	# ----------------------------------------------------------------------------------------- #
		
	if tp.get() <= 0:
		mf.fill(blanc)
		texte = (
				[['Vous n\'avez plus de temps !'], black, None],
				[['Votre score est de ', ss.getScore()], black, None]
			)
		tt.affiche2(texte, center=True, titre=['Game Over !', rouge])
		pygame.display.flip()
		pygame.time.delay(DELAY_MIN_MESSAGE)
		pygame.event.clear(KEYDOWN)
		to.waitForKeydown()
		ss.reset()
		tp.init(TEMPS_DEBUT)


	# ----------------------------------------------------------------------------------------- #
	# -------------------- On verifie que le serpent ne touche pas un bord -------------------- #
	# ----------------------------------------------------------------------------------------- #
	if not ss.move():
		# ss.move() retourne False si le serpent touche un cote de la fenetre (donc qu on perd)
		mf.fill(-1) # on efface l ecran pour qu on ne voit que le message
		# message 
		texte = 'Les murs, ca fait mal !\n' ,'Ne touche pas les bords la prochaine fois !', '\nVotre score est de ', ss.getScore()
		texte = (
			[['Les murs, ca fait mal !'], noir, None],
			[['Ne touche pas les bords la prochaine fois !'], noir, None],
			[['Votre score est de ', ss.getScore()], noir, None]
			)
		tt.affiche2(texte, center=True, titre=['Game Over !', red])
		tt.UTPC()
		pygame.display.flip()
		pygame.time.delay(DELAY_MIN_MESSAGE)
		# on retire tout les event KEYDOWN de la queue
		pygame.event.clear(KEYDOWN)
		to.waitForKeydown()
		ss.reset()
		tp.init(TEMPS_DEBUT) # on remet le temps a 0

	# ------------------------------------------------------------------------ #
	# --------------------------------- Test --------------------------------- #
	# ------------------------------------------------------------------------ #

	
	pygame.display.flip()
	pygame.time.delay(DELAY)