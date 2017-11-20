import unittest

from game import Combat, Equipment
from game.Equipment import Equipment


class EquipmentTestCase(unittest.TestCase):

	def testEquip(self):
		e = Equipment()
		self.assertEquals(None, e[Equipment.RIGHT_HAND])
		self.assertEquals(None, e[Equipment.LEFT_HAND])

		e.equip(Equipment.RIGHT_HAND, Combat.weapons['Dagger'])
		self.assertEquals(Combat.weapons['Dagger'], e[Equipment.RIGHT_HAND])
		self.assertEquals(None, e[Equipment.LEFT_HAND])

		e.equip(Equipment.LEFT_HAND, Combat.weapons['Glaive'])
		self.assertEquals(Combat.weapons['Dagger'], e[Equipment.RIGHT_HAND])
		self.assertEquals(Combat.weapons['Glaive'], e[Equipment.LEFT_HAND])

		e.equip(Equipment.LEFT_HAND, Combat.weapons['Shortbow'])
		self.assertEquals(Combat.weapons['Shortbow'], e[Equipment.RIGHT_HAND])
		self.assertEquals(None, e[Equipment.LEFT_HAND])

	def testEquipInvalidSlot(self):
		with self.assertRaises(ValueError):
			e = Equipment()
			e.equip('foobar', self)

	def testEquipNonWeaponInHands(self):
		with self.assertRaises(ValueError):
			e = Equipment()
			e.equip(Equipment.LEFT_HAND, self)

	def testEquipWeaponWrongSlot(self):
		with self.assertRaises(ValueError):
			e = Equipment()
			e.equipWeapon(Equipment.HEAD, Combat.weapons['Dagger'])

	def testEquipRightHandedInLeftHand(self):
		with self.assertRaises(ValueError):
			e = Equipment()
			e.equip(Equipment.LEFT_HAND, Combat.weapons['Dagger'])

