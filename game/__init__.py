import math
import random

class Dice(object):
	def __init__(self, faces):
		self.faces = faces

	def roll(self, count = 1):
		c = 0
		for i in xrange(count):
			c += random.randint(1, self.faces)
		return c

	def rollAndRemoveWorst(self, dices):
		all = []
		all[:] = (self.roll() for i in xrange(dices))

		best = []
		minFound = False
		m = min(all)
		for i in xrange(4):
			if not minFound and all[i] == m:
				minFound = True
				continue
			best.append(all[i])
		return best


class Ability(object):
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	@property
	def modifier(self):
		return int(math.floor(-5 + self.score  / 2))

	def __str__(self):
		return str(self.score)

class Abilities(object):

	all = [
		'Strength', 'Dexterity', 
		'Constitution', 'Intelligence', 
		'Wisdom', 'Charisma'
	]

	def __init__(self, scores = False):

		self._all = {}

		if scores and len(scores) != len(Abilities.all):
			raise ValueError('Score must be an array of %s elements' % len(self.all))

		for i in xrange(0, len(Abilities.all)):
			name = Abilities.all[i];
			score = 0 if not scores else scores[i]
			self._all[name] = Ability(name, score)

	def get(self, name):
		if not name in Abilities.all:
			raise IndexError('Invalid ability: ' + name)
		return self._all[name]

	def roll(self):
		for i in xrange(0, len(Abilities.all)):
			name = Abilities.all[i];
			self._all[name] = Ability(name, score)

	def _randomScore(self):
		pass
