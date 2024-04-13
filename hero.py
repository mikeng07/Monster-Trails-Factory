import entity
import random

class Hero(entity.Entity):
    """character that the user plays"""
    def __init__(self,name):
        """set hero name, starting hp, and location"""
        super().__init__(name,25)

    def melee_attack(self,entity):
        """attack opposing enemy and return description"""
        dmg = random.randint (1,6) + random.randint(1,6)
        entity.take_damage(dmg)
        return self._name + " slashes a " + entity.name + " with a sword for " + str(dmg) + " damage."

    def ranged_attack(self, entity):
        dmg = random.randint(1,12)
        entity.take_damage(dmg)
        return self._name + " pierces a " + entity.name + " with a arrow for " + str(dmg) + " damage."