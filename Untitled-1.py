from numpy.random import choice
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
    enemies = [rat,goblin,demon,dragon]
    randomEnemy = choice(enemies,1,p=[0.4,0.3,0.2,0.1])
    print ("{} attacked you!!!".format(randomEnemy.name))
encounter()
print ("Game over!")
