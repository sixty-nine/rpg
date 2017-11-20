from Combat import Damage
from game import Abilities

class Monster(object):

	def __init__(self, name, damage, abilityScores = False, initiative = 1, speed = 1, ac = 1, description = ''):
		self.name = name
		self.description = description
		self.ac = ac
		self.initiative = initiative
		self.damage = damage
		self.abilities = Abilities(abilityScores)
		self.speed = speed

	def dump(self):
		print 'Monster: ' + self.name
		print 'Damage: ' + str(self.damage)
		print 'Speed: ' + str(self.speed)
		print 'Abilities:'
		for name in Abilities.all:
			print  '  ' + name + ': ' + str(self.abilities[name]) + ' / ' + str(Abilities.modifier(self.abilities[name]))

monsters = [
	Monster('Naga', Damage(8, 9, 18), abilityScores = [14, 15, 14, 16, 15, 17], initiative = 2, speed = 40, ac = 14),
	Monster('Goblin', Damage(8, 1, 1), abilityScores = [11, 13, 12, 10, 9, 6], speed = 30, ac = 15),
]
