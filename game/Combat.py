from game import Dice, Abilities
from Equipment import Weapon, Equipment
from Characters import Creature, Character

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

class Combat(object):

	def __init__(self, attacker, defender):
		if not isinstance(attacker, Creature):
			raise ValueError('Attacker must be a creature')
		if not isinstance(defender, Creature):
			raise ValueError('Defender must be a creature')

		self.attacker = attacker
		self.defender = defender

	def order(self):
		if not self.attacker.firstStrike:
			if self.defender.firstStrike or self.defender.initiative > self.attacker.initiative:
				return [self.defender, self.attacker]

		return [self.attacker, self.defender]

	def doRound(self):

		(first, second) = self.order()

		self._attack(first, second)
		self._attack(second, first)

	def _attack(self, attacker, defender):
		if attacker.isDead:
			return

		if isinstance(attacker, Character):
			if attacker.equipment[Equipment.RIGHT_HAND]:
				self._doAttack(attacker, defender, attacker.equipment[Equipment.RIGHT_HAND])
			if not defender.isDead and attacker.equipment[Equipment.LEFT_HAND]:
				self._doAttack(attacker, defender, attacker.equipment[Equipment.LEFT_HAND])
		else:
			self._doAttack(attacker, defender)

	def _doAttack(self, me, other, weapon = None):

		if isinstance(me, Character):
			if not isinstance(weapon, Weapon):
				raise ValueError('You can only attack with weapons')
			ability = Abilities.STRENGTH if not weapon.isRanged else Abilities.DEXTERITY
			modifier = Abilities.modifier(me.abilities[ability])
			threatRange = weapon.threatRange
			damages = weapon.damage
			criticalDmg = weapon.critical
		else:
			modifier = 0
			threatRange = 20
			damages = me.damage
			criticalDmg = 2

		attackRoll = Dice(20).roll()
		threatRange = threatRange
		critical = attackRoll >= threatRange

		print '--'
		print '-- %s attacks %s' % (me.name, other.name)

		print '-- Dice roll: %s + %s = %s' % (attackRoll, modifier, attackRoll + modifier)

		if attackRoll == 1:
			print '-- Critical miss'
			return

		attackRoll += modifier
		touch = attackRoll >= other.ac

		if not touch:
			print '-- Miss'
			return

		dmg = damages.calc()
		totalDmg = dmg + modifier
		if not critical:
			print '-- Damage dealt: %s + %s = %s' % (dmg, modifier, totalDmg)
		else:
			totalDmg *= criticalDmg
			print '-- Critical damage dealt: %s * (%s + %s) = %s' % (criticalDmg, dmg, modifier, totalDmg)

		other.hp -= totalDmg

		if other.hp > 0:
			print '-- %s HP: %s' % (str(other.name), other.hp)
		else:
			print '-- %s is dead' % other.name


weapons = {
	'Gauntlet': Weapon('Gauntlet', Damage(2)),
	'Dagger': Weapon('Dagger', Damage(3), threatRange = 19),
	'Falchion': Weapon('Falchion', Damage(6), threatRange = 18),
	'Glaive': Weapon('Glaive', Damage(6), critical = 3, rightHanded = False),
	'Glaive of strength': Weapon('Glaive of strength', Damage(6, 2, 5), critical = 3, rightHanded = False, minLevel = 10),
	'Shortbow': Weapon('Shortbow', Damage(6), critical = 3, range = 50, doubleHanded = True),
	'Longbow': Weapon('Longbow', Damage(8), critical = 3, range = 100, doubleHanded = True),
}	

