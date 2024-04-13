import abc
import entity
class EnemyFactory(abc.ABC):
    """Interface for Enemy Factories"""
    @abc.abstractmethod
    def create_random_enemy(self)->entity.Entity:
        #type hint: should return an object of Entity
        pass