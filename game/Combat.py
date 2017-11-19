from game import Dice;

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

class Weapon(object):

	def __init__(self, name, damage, description = '', threatRange = 20, critical = 2, range = 0, weight = 0):
		self.name = name 
		self.damage = damage
		self.description = description
		self.threatRange = threatRange
		self.critical = critical
		self.range = range
		self.weight = weight

	@property
	def isRanged(self):
		return self.range > 0

	def __str__(self):
		critical = ('20' if self.threatRange == 20 else str(self.threatRange) + '-20') + '/x' + str(self.critical) 
		data = {'name': self.name, 'damage': self.damage, 'critical': critical}
		props = '%(name)s, dmg: %(damage)s, crit: %(critical)s' % data
		if self.isRanged: props += ', Range: %sm' % (self.range)
		return 'WEAPON(%(props)s)' % {'props': props}

weapons = [
	Weapon('Gauntlet', Damage(2)),
	Weapon('Dagger', Damage(3), threatRange = 19),
	Weapon('Falchion', Damage(6), threatRange = 18),
	Weapon('Glaive', Damage(6), critical = 3),
	Weapon('Glaive of strength', Damage(6, 2, 5), critical = 3),
	Weapon('Shortbow', Damage(6), critical = 3, range = 50),
	Weapon('Longbow', Damage(8), critical = 3, range = 100),
]	

