import entity
import random

class ExpTroll(entity.Entity):
    """represent an expert troll enemy"""
    def __init__(self):
        """create an expert troll"""
        super().__init__("Tremendous Troll", random.randint(15,18))

    def melee_attack(self,entity):
        """acttack the opposing enemy and return description"""
        dmg = random.randint(8,12)
        entity.take_damage(dmg)
        return self._name + " whacks " + entity.name + " for " + str(dmg) + " damage."