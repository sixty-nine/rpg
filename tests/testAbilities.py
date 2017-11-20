import unittest

from game import Abilities

class AbilitiesTestCase(unittest.TestCase):

	def testInit(self):
		a = Abilities()
		for name in Abilities.all:
			self.assertEquals(0, a[name])

	def testInitWithDefaults(self):
		a = Abilities(scores = [1, 2, 3, 4, 5, 6])
		counter = 1
		for name in Abilities.all:
			self.assertEquals(counter, a[name])
			counter += 1

	def testInitWithInvalidDefaults(self):
		with self.assertRaises(ValueError):
			a = Abilities([1])

	def testKeys(self):
		a = Abilities()
		self.assertItemsEqual(a.keys(), Abilities.all)

	def testGetSetItem(self):
		a = Abilities()
		self.assertEquals(0, a['Strength'])
		a['Strength'] = 10
		self.assertEquals(10, a['Strength'])

	def testGetItemError(self):
		with self.assertRaises(IndexError):
			a = Abilities()
			b = a['foobar']

	def testSetItemError(self):
		with self.assertRaises(IndexError):
			a = Abilities()
			a['foobar'] = 0

	def testIter(self):
		a = Abilities([123, 123, 123, 123, 123, 123])
		for name, value in a:
			self.assertIn(name, Abilities.all)
			self.assertEquals(123, value)

	def testRandom(self):
		class Strategy(object):
			def roll(self):
				return 123
		a = Abilities()
		a.random(Strategy())
		for name, value in a:
			self.assertIn(name, Abilities.all)
			self.assertEquals(123, value)

	def testRandomWrongStrategy(self):
		with self.assertRaises(ValueError):
			a = Abilities()
			a.random(self)

	def testModifier(self):
		self.assertEquals(-5, Abilities.modifier(0))
		self.assertEquals(-5, Abilities.modifier(1))
		self.assertEquals(-3, Abilities.modifier(5))
		self.assertEquals(0, Abilities.modifier(10))
		self.assertEquals(4, Abilities.modifier(19))
		self.assertEquals(5, Abilities.modifier(20))
