#Monster Trail game

import hero
import beg_factory
import exp_factory
import check_input

def main():
    print("Monster trails")
    name = input("what is your name? ")
    print("you will face a series of 3 monster, " + name + ".\nDefeat them all to win.")
    h = hero.Hero(name)
    enemies = []

    #create 2 easy enemies and 1 difficult enemy
    fact = beg_factory.BeginerFactory()
    enemies.append(fact.create_random_enemy())
    enemies.append(fact.create_random_enemy())
    fact = exp_factory.ExpertFactory()
    enemies.append(fact.create_random_enemy())

    #play game until hero dies all defeats all enemies
    while len(enemies) > 0 and h.hp > 0:
        print("Choose an enemy to attack:")
        for i in range(len(enemies)):
            print(str(i + 1) + ". " + str(enemies[i]))
        enemy = check_input.get_int_range("Enter choice: ", 1, len(enemies)) - 1
        print(h)
        print("1. Sword Attact")
        print("2. Arrow Attack")
        atk = check_input.get_int_range("Enter choice: ",1,2)
        if atk ==1:
            print(h.melee_attack(enemies[enemy]))
        else:
            print(h.ranged_attack(enemies[enemy]))
        if enemies[enemy].hp > 0:
            print(enemies[enemy].melee_attack(h))
        else:
            print("You hav slain the "+ enemies[enemy].name)
            enemies.pop(enemy)
    if h.hp == 0:
        print ("you have been defeated.")
    else:
        print("Congratulation! You defeated all the three monsters.")
    print("Game Over")

main() 