import abc
class Entity(abc.ABC):
    """Characters in the dungeon game."""
    def __init__(self,name,hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        """access entity's name"""
        return self._name

    @property
    def hp(self):
        """access entity's hp"""
        return self._hp

    def take_damage(self,dmg):
        """substracts from entity's hp."""
        self._hp -= dmg
        if self._hp < 0 :
            self._hp = 0 

    def __str__(self):
        """string representataion of an entity"""
        return self._name + " HP: " + str(self._hp)

    @abc.abstractmethod
    def melee_attack(self,entity):
        """attacks the opposing entity"""
        pass 