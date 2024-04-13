import entity
import random

class ExpGoblin(entity.Entity):
    """represent an expert goblin enemy"""
    def __init__(self):
        """create an easy goblin"""
        super().__init__("Vicious", random.randint(12,15))

    def melee_attack(self,entity):
        """acttack the opposing enemy and return description"""
        dmg = random.randint(5,8)
        entity.take_damage(dmg)
        return self._name + " attacks " + entity.name + " for " + str(dmg) + " damage."