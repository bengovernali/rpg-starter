"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from random import randint

class Character:
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty
    
    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):
        
        #probability shadow doesn't get hit
        if enemy.type == 'shadow':
            hit_chance = randint(1, 10)
            if hit_chance != 10:
                print('Attack missed!')
                return

        #add crit hit chance for hero
        if self.type == 'hero':
            crit_val = randint(0, 100)
            if crit_val >= 80:
                damage = self.power * 2
            else:
                damage = self.power
        else:
            damage = self.power
        
        #standard attack operation
        if enemy.type != 'zombie':
            enemy.health -= damage
        print("{} does {} damage to {}.".format(self.name, damage, enemy.name))
        if enemy.health <= 0:
            print("{} is dead. {} receives {} gold for winning".format(enemy.name, self.name, enemy.bounty))
        
        #chance that medic can heal self after attack
        if enemy.type == 'medic':
            heal_chance = randint(0, 100)
            if heal_chance >= 80:
                enemy.health += 2
                print("The Medic healed for 2 points!")

class Hero(Character):
    type = 'hero'

class Goblin(Character):
    type = 'goblin'

class Zombie(Character):
    type = 'zombie'
    def alive(self):
        return True

class Medic(Character):
    type = 'medic'

class Shadow(Character):
    type = 'shadow'
    
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = 1
        self.power = power

thor = Hero('Thor', 10, 5, 50)
thrym = Goblin('Thrym', 6, 2, 30)
brains = Zombie('Braaaaaaiiiiinnnnnsss', 20, 4, 0)
dark_link = Shadow('Dark Link', 3, 2, 5)
regenero = Medic('Regenero', 10, 1, 15)

def main():

    player = thor
    foe = dark_link
    
    while foe.alive() and player.alive():
        player.print_status()
        foe.print_status()
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks enemy
            player.attack(foe)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if foe.health > 0:
            # Enemy attacks hero
            foe.attack(player)

main()