import entity
import random

class BegTroll(entity.Entity):
    """represent an beginer troll enemy"""
    def __init__(self):
        """create an easy troll"""
        super().__init__("Troll", random.randint(8,10))

    def melee_attack(self,entity):
        """acttack the opposing enemy and return description"""
        dmg = random.randint(5,9)
        entity.take_damage(dmg)
        return self._name + " crushes " + entity.name + " for " + str(dmg) + " damage."