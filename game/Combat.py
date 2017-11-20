from game import Dice
from Equipment import Weapon

class Damage(object):

	def __init__(self, diceType = 6, diceCount = 1, modifier = 0):
		self.dice = Dice(diceType)
		self.diceCount = diceCount
		self.modifier = modifier

	def calc(self):
		return self.dice.roll(self.diceCount) + self.modifier

	def min(self):
		return self.diceCount + self.modifier

	def max(self):
		return self.diceCount * self.dice.faces + self.modifier

	def __str__(self):
		return '[%(min)s-%(max)s]' % {'min': self.min(), 'max': self.max()}

weapons = {
	'Gauntlet': Weapon('Gauntlet', Damage(2)),
	'Dagger': Weapon('Dagger', Damage(3), threatRange = 19),
	'Falchion': Weapon('Falchion', Damage(6), threatRange = 18),
	'Glaive': Weapon('Glaive', Damage(6), critical = 3, rightHanded = False),
	'Glaive of strength': Weapon('Glaive of strength', Damage(6, 2, 5), critical = 3, rightHanded = False, minLevel = 10),
	'Shortbow': Weapon('Shortbow', Damage(6), critical = 3, range = 50, doubleHanded = True),
	'Longbow': Weapon('Longbow', Damage(8), critical = 3, range = 100, doubleHanded = True),
}	

