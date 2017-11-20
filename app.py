#!/usr/local/bin/python

import argparse
import sys

from game import Combat, Monsters, Characters
from game.Equipment import Equipment
from game.Characters import Character

FLAGS = None

def main(_):
	print '-' * 80
	for weapon in Combat.weapons:
		print str(Combat.weapons[weapon])
	print '-' * 80

	for monster in Monsters.monsters:
		monster.dump()
		print '-' * 80

	p = Character('Letitbi', speed = 30)
	p.randomize()
	p.equip(Equipment.RIGHT_HAND, Combat.weapons['Dagger'])
	p.equip(Equipment.LEFT_HAND, Combat.weapons['Glaive'])
	p.dump()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  #parser.add_argument('--set', type=str, default='train', help='The data set to use (train, test, validation)')
  #parser.add_argument('--max', type=int, default=1, help='How many images to show')
  FLAGS, unparsed = parser.parse_known_args()
  main([sys.argv[0]] + unparsed)
