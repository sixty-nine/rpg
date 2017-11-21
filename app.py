#!/usr/local/bin/python

import argparse
import sys

from game import Combat, Monsters, Characters
from game.Equipment import Equipment
from game.Characters import Character
from game.markov import NameGenerator, males, females

FLAGS = None

def main(_):

	if FLAGS.dump_weapons:
		print '-' * 80
		for weapon in Combat.weapons:
			print str(Combat.weapons[weapon])
		print '-' * 80
		return

	if FLAGS.dump_monsters:
		for name, monster in Monsters.monsters.iteritems():
			monster.dump()
			print '-' * 80
		return

	m = Monsters.monsters['Goblin']

	name = NameGenerator(males + females).generate()
	p = Character(name, speed = 30)
	p.randomize()
	p.equip(Equipment.RIGHT_HAND, Combat.weapons['Dagger'])
	p.equip(Equipment.LEFT_HAND, Combat.weapons['Glaive'])
	p.dump()

	if FLAGS.combat:
		c = Combat.Combat(p, m)
		while not p.isDead and not m.isDead:
			c.doRound()
		print p.name, p.hp
		print m.name, m.hp


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--dump-weapons', action='store_true', help='Dump the weapons')
	parser.add_argument('--dump-monsters', action='store_true', help='Dump the monsters')
	parser.add_argument('--combat', action='store_true', help='Engage a fight')
	#parser.add_argument('--max', type=int, default=1, help='How many images to show')
	FLAGS, unparsed = parser.parse_known_args()
	main([sys.argv[0]] + unparsed)
