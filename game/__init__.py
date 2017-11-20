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

		for i in xrange(dices):
			if not minFound and all[i] == m:
				minFound = True
				continue
			best.append(all[i])
		return best

class Roll4AndRemoveWorstStrategy(object):
	def roll(self):
		return sum(Dice(6).rollAndRemoveWorst(4))

class Abilities(object):

	STRENGTH = 'Strength'
	DEXTERITY = 'Dexterity'
	CONSTITUTION = 'Constitution'
	INTELLIGENCE = 'Intelligence'
	WISDOM = 'Wisdom'
	CHARISMA = 'Charisma'

	all = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM, CHARISMA]

	@staticmethod
	def modifier(score):
		return int(math.floor(-5 + score  / 2))

	def __init__(self, scores = False):

		self._all = {}

		if scores and len(scores) != len(Abilities.all):
			raise ValueError('Score must be an array of %s elements' % len(self.all))

		for i in xrange(0, len(Abilities.all)):
			name = Abilities.all[i];
			score = 0 if not scores else scores[i]
			self._all[name] = score

	def keys(self):
		return self._all.keys()

	def __getitem__(self, key):
		self.ensureAbilityName(key)
		return self._all[key]

	def __setitem__(self, key, value):
		self.ensureAbilityName(key)
		self._all[key] = value

	def __iter__(self):
		return self._all.iteritems()

	def __str__(self):
		s = '';
		for name in Abilities.all:
			s += ', ' if s != '' else ''
			s += '%s: %s' % (name[:3], self._all[name])
		return '(' + s + ')'

	def ensureAbilityName(self, name):
		if not name in Abilities.all:
			raise IndexError('"%s" is not an ability name' % name)

	def random(self, strategy):
		if not 'roll' in dir(strategy):
			raise ValueError('The strategy must have a roll() method')
		for name in Abilities.all:
			self._all[name] = strategy.roll()


from . import Equipment

