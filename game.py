"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker: Character, defender: Character):
	weapon_used = attacker.spell if isinstance(attacker, Magician) and attacker.will_use_spell() else attacker.weapon
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"{attacker.name} used {weapon_used.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1: Character, c2: Character):
	pass
