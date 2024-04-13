import enemy_factory
import beg_troll
import beg_goblin
import random

class BeginerFactory(enemy_factory.EnemyFactory):
    """Factory for creating easy enemies."""
    def create_random_enemy(self):
        rand = random.randint(1,2)
        if rand == 1:
            return beg_troll.BegTroll()
        else:
            return beg_goblin.BegGoblin()

            