import random
from game import Abilities, Dice

class CharacterClass(object):

	def __init__(self, name, hitDie, skillPointsPerLevel = 2):
		self.name = name
		self.hitDie = hitDie
		self.skillPointsPerLevel = skillPointsPerLevel

	def getSkillPointsPerLevel(self, intModifier):
		return self.skillPointsPerLevel + intModifier
	def getInitialSkillPoints(self, intModifier):
		return self.getSkillPointsPerLevel(intModifier) * 4

classes = [
	CharacterClass('Barbarian', Dice(12), skillPointsPerLevel = 4),
	CharacterClass('Fighter', Dice(10)),
	CharacterClass('Rogue', Dice(6), skillPointsPerLevel = 8),
	CharacterClass('Sorcerer', Dice(4)),
]

class Race(object):

	def __init__(self, name, attrModifiers = [0, 0, 0, 0, 0, 0]):
		self.name = name
		self.attrModifiers = attrModifiers

races = [
	Race('Human'),
	Race('Dwarf', attrModifiers = [0, 0, 2, 0, 0, -2]),
	Race('Elf', attrModifiers = [0, 2, -2, 0, 0, 0]),
	Race('Gnome', attrModifiers = [-2, 0, 2, 0, 0, 0]),
	Race('Half-Elf'),
	Race('Half-Orc', attrModifiers = [2, 0, 0, -2, 0, -2]),
	Race('Halfling', attrModifiers = [-2, 2, 0, 0, 0, 0]),
]

class Character(object):
	def __init__(self, name, abilityScores = False, initiative = 1, speed = 1, ac = 1, charClass = False, race = False):
		self.level = 1
		self.name = name
		self.ac = ac
		self.initiative = initiative
		self.abilities = Abilities(abilityScores)
		self.speed = speed
		self.charClass = charClass if charClass else random.choice(classes)
		self.setRace(race)

	def randomize(self):
		self.charClass = random.choice(classes)
		for i, name in enumerate(Abilities.all):
			self.abilities.get(name).score = sum(Dice(6).rollAndRemoveWorst(4))
		self.setRace(random.choice(races))

	def setRace(self, race):
		self.race = race
		if race:
			for i, name in enumerate(Abilities.all):
				self.abilities.get(name).score += self.race.attrModifiers[i]		

	def dump(self):
		print 'Character: ' + self.name
		print 'Race: ' + self.race.name + ', ' + str(self.race.attrModifiers)
		print 'Class: ' + self.charClass.name + ', sp/level = ' + \
			str(self.charClass.getSkillPointsPerLevel(self.abilities.get('Intelligence').modifier))
		print 'Speed: ' + str(self.speed)
		print 'Abilities:'
		for name in Abilities.all:
			print  '  ' + name + ': ' + str(self.abilities.get(name)) + ' / ' + str(self.abilities.get(name).modifier)

p = Character('Letitbi', speed = 30)
p.randomize()
p.dump()

print Dice(6).rollAndRemoveWorst(4)
