class Item(object):

	def __init__(self, name, description = '', minLevel = 0, weight = 0):
		self.minLevel = minLevel
		self.name = name
		self.description = description
		self.weight = weight

class Weapon(Item):

	def __init__(self, name, damage, description = '', minLevel = 0, \
				 threatRange = 20, critical = 2, range = 0, weight = 0, rightHanded = True, doubleHanded = False):
		super(Weapon, self).__init__(name, description = description, minLevel = minLevel, weight = weight)
		self.doubleHanded = doubleHanded
		self.rightHanded = True if doubleHanded else rightHanded
		self.damage = damage
		self.threatRange = threatRange
		self.critical = critical
		self.range = range

	@property
	def isRanged(self):
		return self.range > 0

	def __str__(self):
		critical = ('20' if self.threatRange == 20 else str(self.threatRange) + '-20') + '/x' + str(self.critical) 
		data = {'name': self.name, 'damage': self.damage, 'critical': critical}
		props = '%(name)s, dmg: %(damage)s, crit: %(critical)s' % data
		if self.isRanged: props += ', Range: %sm' % (self.range)
		if self.doubleHanded: props += ', Double-Handed'
		if self.rightHanded and not self.doubleHanded: props += ', Right-Handed'
		if self.minLevel > 0: props += ', minLevel = ' + str(self.minLevel)
		return 'WEAPON(%(props)s)' % {'props': props}

class Equipment(object):

	RIGHT_HAND = 'Right Hand'
	LEFT_HAND = 'Left Hand'
	HEAD = 'Head'

	allSlots = [RIGHT_HAND, LEFT_HAND, HEAD]
	weaponsSlots = [RIGHT_HAND, LEFT_HAND]

	def __init__(self):
		self._slots = {}
		self.unequipAll()

	def __getitem__(self, key):
		self.ensureValidSlot(key)
		return self._slots[key]

	def unequipAll(self):
		for slot in Equipment.allSlots:
			self._slots[slot] = None

	def equip(self, slot, item):
		self.ensureValidSlot(slot)
		if not isinstance(item, Item):
			raise ValueError('You must equip an item')

		if (slot in Equipment.weaponsSlots):
			self.equipWeapon(slot, item)

	def equipWeapon(self, slot, weapon):
		if not isinstance(weapon, Weapon):
			raise ValueError('You must equip a weapon in your hands')

		if not slot in Equipment.weaponsSlots:
			raise ValueError('The hand can be "%s" or "%s"' % (Equipment.RIGHT_HAND, Equipment.LEFT_HAND))

		if weapon.doubleHanded:
			self.unequipAll()
			slot = Equipment.RIGHT_HAND

		if slot == Equipment.LEFT_HAND and weapon.rightHanded:
			raise ValueError('The weapon %s cannot be held in left hand' % weapon.name)

		self._slots[slot] = weapon

	def ensureValidSlot(self, slot):
		if not slot in Equipment.allSlots:
			raise ValueError('Invalid slot: ' + slot)		

	def dump(self):
		print 'Equipment:'
		for name, value in self._slots.iteritems():
			print '  ' + name + ': ' + ('-' if value is None else str(value))
