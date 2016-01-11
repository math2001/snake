from random import randint
l = ['liste', 'lol']
a = ['coucou', 'lo']
b = ['ce', 'autre']

z = a + l + b
def _choisi_bonbon(liste):
	""" Cette fonction choisi un bonbon dans liste en le retirant """
	LL = len(liste)
	if LL > 0:
		index = randint(0, LL - 1)
		bonbon = liste.pop(index)
	else:
		bonbon = None
	return bonbon, liste

liste = ['M', 'a', 't', 'h', '2', '0', '0', '1']
for i in range(50):
	# if len(z) > 0:
	# 	nb = randint(0, len(z) - 1)
	# 	print z.pop(nb)
	bonbon, liste = _choisi_bonbon(liste)
	print bonbon, liste