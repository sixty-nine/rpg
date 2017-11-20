from Combat import Damage
from Characters import Creature
from game import Abilities

class Monster(Creature):

	def __init__(self, name, damage, abilityScores = False, initiative = 1, speed = 1, ac = 1, description = '', hp = 1, firstStrike = False):
		super(Monster, self).__init__(name, abilityScores = abilityScores, initiative = initiative, ac = ac, hp = hp, firstStrike = firstStrike)
		self.description = description
		self.damage = damage
		self.abilities = Abilities(abilityScores)
		self.speed = speed

	def dump(self):
		print 'Monster: ' + self.name
		print 'HP: ' + str(self.hp)
		print 'AC: ' + str(self.ac)
		print 'Initialive: ' + str(self.initiative)
		print 'Damage: ' + str(self.damage)
		print 'Speed: ' + str(self.speed)
		print 'Abilities:'
		for name in Abilities.all:
			print  '  ' + name + ': ' + str(self.abilities[name]) + ' / ' + str(Abilities.modifier(self.abilities[name]))

monsters = {
	'Naga': Monster('Naga', Damage(8, 9, 18), abilityScores = [14, 15, 14, 16, 15, 17], initiative = 2, speed = 40, ac = 14, hp = 58),
	'Goblin': Monster('Goblin', Damage(8, 1, 1), abilityScores = [11, 13, 12, 10, 9, 6], speed = 30, ac = 15, hp = 6),
}
