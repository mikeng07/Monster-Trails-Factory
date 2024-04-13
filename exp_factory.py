import enemy_factory
import exp_troll
import exp_goblin
import random

class ExpertFactory(enemy_factory.EnemyFactory):
    """factory for creating defficult enemy """
    def create_random_enemy(self):
        """contruct and return a random difficult enemy"""
        rand = random.randint(1,2)
        if rand == 1:
            return exp_troll.ExpTroll()
        else:
            return exp_goblin.ExpGoblin()

            