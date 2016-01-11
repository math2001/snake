class Class:
	def __init__(self):
		self.me = 'message !'

	class Big:
		def __init__(self, mere):
			self.mere = mere
		def lol(self):
			print 'lol ' + self.mere.me

c = Class()
b = c.Big(c)
print c
print b

b.lol()