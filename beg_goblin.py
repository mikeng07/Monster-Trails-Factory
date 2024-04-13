import entity
import random

class BegGoblin(entity.Entity):
    """represent an beginer goblin enemy"""
    def __init__(self):
        """create an easy goblin"""
        super().__init__("Goblin", random.randint(7,9))

    def melee_attack(self,entity):
        """acttack the opposing enemy and return description"""
        dmg = random.randint(4,6)
        entity.take_damage(dmg)
        return self._name + " bites " + entity.name + " for " + str(dmg) + " damage."