import unittest

from game import Dice

class DiceTestCase(unittest.TestCase):

	def testDice10(self):
		d = Dice(10)
		for i in xrange(100):
			roll = d.roll()
			self.assertGreaterEqual(roll, 0)
			self.assertLessEqual(roll, 10)

	def testDice10(self):
		d = Dice(100)
		for i in xrange(100):
			roll = d.roll()
			self.assertGreaterEqual(roll, 0)
			self.assertLessEqual(roll, 100)

	def testRollAndRemoveWorst(self):

		for i in xrange(2, 100):
			d = Dice(6)
			res = d.rollAndRemoveWorst(i)
			self.assertEquals(i - 1, len(res), 'Not enough results, expected %s, got %s, with %s' % (i - 1, len(res), res))
			self.assertGreaterEqual(sum(res), i - 1, 'Expected %s to be greater than %s, with %s' % (sum(res), i - 1, res))
			self.assertLessEqual(sum(res), 6 * i)
