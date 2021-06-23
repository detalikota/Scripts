from numpy.random import choice
from random import randint

class Char:
    def __init__(self, spec, name, strength, magic, health, gold):
        self.spec = spec
        self.name = name
        self.strength = strength
        self.magic = magic
        self.health = health
        self.gold = gold
    def strengthUp(self, amount):
        self.strength += amount
    def strengthDown(self, amount):
        self.strength -= amount
    def magicUp(self, amount):
        self.magic += amount
    def magicDown(self, amount):
        self.magic -= amount
    def healthUp(self, amount):
        self.health += amount
    def healthDown(self, amount):
        self.health -= amount
    def goldUp(self, amount):
        self.gold += amount
    def goldDown(self, amount):
        self.gold -= amount
    def stats(self):
        print("{}, your {} have {} strength, {} magic, {} health and {} gold".format(self.name,self.spec,self.strength,self.magic,self.health,self.gold))
class Enemy:
    def __init__(self,name, strength, magic, health, gold):
        self.name = name
        self.strength = strength
        self.magic = magic
        self.health = health
        self.gold = gold
    def strengthUp(self, amount):
        self.strength += amount
    def strengthDown(self, amount):
        self.strength -= amount
    def magicUp(self, amount):
        self.magic += amount
    def magicDown(self, amount):
        self.magic -= amount
    def healthUp(self, amount):
        self.health += amount
    def healthDown(self, amount):
        self.health -= amount
    def stats(self):
        print("{}, your {} have {} strength, {} magic, {} health and {} gold".format(self.name,self.spec,self.strength,self.magic,self.health,self.gold))
class Ally:
    def __init__(self, name, strength, magic, health, gold):
        self.name = name
        self.strength = strength
        self.magic = magic
        self.health = health
        self.gold = gold
    def strengthUp(self, amount):
        self.strength += amount
    def strengthDown(self, amount):
        self.strength -= amount
    def magicUp(self, amount):
        self.magic += amount
    def magicDown(self, amount):
        self.magic -= amount
    def healthUp(self, amount):
        self.health += amount
    def healthDown(self, amount):
        self.health -= amount
    def stats(self):
        print("{}, your {} have {} strength, {} magic, {} health and {} gold".format(self.name,self.spec,self.strength,self.magic,self.health,self.gold))
print("1. Dwarf\n2. Elf\n3. Barbarian")
choose = input("Choose your character: ")
name = input("Input your character name: ")
if choose == '1' or 'Dwarf' or 'dwarf':
    char = Char('Dwarf', name, 7, 3, 10, 50)
elif choose == '2' or 'Elf' or 'elf':
        char = Char('Elf', name, 5, 9, 5, 80)
elif choose == '3' or 'Barbarian' or 'barbarian':
    char = Char('Barbarian', name, 10, 2, 9, 30)
print("Your stats are:\nStrength: {}\nMagic: {}\nHealth: {}\nGold: {}".format(char.strength,char.magic,char.health,char.gold))
print("You can add up to 5 additional points")
points = 5
while points > 0:
    print("How many points do you want to add to Strength?")
    while True:
        print("Your have {} points left".format(points))
        sup = int(input())
        if sup >points:
            print("Too many points!")
        else: 
            break
    points -= sup
    char.strengthUp(sup)
    print("How many points do you want to add to Health?")
    if points == 0:
            break
    while True:
        print("Your have {} points left".format(points))
        hup = int(input())
        if hup >points:
            print("Too many points!")
        else: 
            break
    points -= hup
    char.healthUp(hup)
    print("How many points do you want to add to Magic?")
    if points == 0:
            break
    while True:
        print("Your have {} points left".format(points))
        mup = int(input())
        if mup >points:
            print("Too many points!")
        else: 
            break
    points -= mup
    char.magicUp(mup)
print ("Your final char stats:")
char.stats()

rat = Enemy('Rat',1,1,5,5)
goblin = Enemy('Goblin',3,4,10,15)
demon = Enemy('Demon',6,6,15,25)
dragon = Enemy('Dragon',10,10,30,50)

villager = Ally('Villager',1,1,5,5)
warrior = Ally('Warrior',3,4,10,15)
paladin = Ally('Paladin',6,6,15,25)
king = Ally('King',15,15,40,1000)

def encounter():
    enemies = [0,1,2,3]
    random= choice(enemies,1,p=[0.4,0.3,0.2,0.1])
    if random[0] == 0:
        enemy = rat
    elif random[0] == 1:
        enemy = goblin
    elif random[0] == 2:
        enemy = demon
    elif random[0] == 3:
        enemy = dragon
    print ("{} attacked you!!!".format(enemy.name))
    input()
    while enemy.health > 0 and char.health > 0:
        whoAttack = randint(0,1)
        if whoAttack == 0:
            print ("{} attacked you for {} damage".format(enemy.name, enemy.strength))
            print ("You lost {} health".format(enemy.strength))
            char.healthDown(enemy.strength)
            if char.health > 0:
                print ("You have {} health left".format(char.health))
            else:
                print ("You died!")
        if whoAttack == 1:
            print ("You attacked {} for {} damage".format(enemy.name, char.strength))
            print ("{} lost {} health".format(enemy.name, char.strength))
            enemy.healthDown(char.strength)
            if enemy.health > 0:
                print ("{} have {} health left".format(enemy.name, enemy.health))
            else:
                print ("{} died!".format(enemy.name))
                if enemy == rat:
                    print("You get 5 gold!")
                    char.goldUp(5)
                if enemy == goblin:
                    print("You get 10 gold!")
                    char.goldUp(10)
                if enemy == demon:
                    print("You get 20 gold!")
                    char.goldUp(20)
                if enemy == dragon:
                    print("You get 50 gold!")
                    char.goldUp(50)
                    input()
    
while char.health>0:
    encounter()
    input()
    
print ("Game over!")