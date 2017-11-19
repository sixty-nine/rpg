# World

## Epoch

	Epoch.current
	Epoch.city
	Epoch.next():
		self.current++
		self.city.produce()

## Economy

	Economy.gold
	Economy.wood
	Economy.food

## City

	City.factories
	City.workers
	City.build(Factory factory)
	City.produce():
		for factory in self.factories:
			factory.produce()

## Factory

	Factory(Economy e)
	Factory.price
	Factory.workers
	Factory.produce()

	Sawmill < Factory
	Sawmill.produce():
		if (e.has(10, 'wood')):
			e.consume(10, 'wood')
			e.produce(10, 'plank')

## Market

MerchandableGood.item
MerchandableGood.sellPrice
MerchandableGood.buyPrice

# Combat

## Fighter

Sizes modifiers:

	Colossal	-8
	Gargantuan	-4
	Huge 		-2
	Large		-1
	Medium		+0
	Small		+1
	Tiny		+2
	Diminutive	+4
	Fine		+8

Abilities = [Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma]
Abilities.getModifier(value):
	return math.floor(-5 + x  / 2) 

Attribute.current
Attribute.max

Fighter.health
Fighter.abilities
Fighter.AC():
	for item in self.equipedItems:
		if item has AC bonus: 

Attack.canTouch(oponent):
	roll = Roll(20)
	if (roll == 1): return false;
	if (roll == 20): return critical;
	else return roll + Abilities.getModifier() >= oponent.AC()

## Weapon

Weapon.name
Weapon.description
Weapon.damage
Weapon.threat_range = 20, 19, 18
Weapon.critical = 2
Weapon.range
Weapon.weight
