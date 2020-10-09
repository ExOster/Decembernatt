from random import *
from time import *


def name():
    namn=input(" Välkommen, Vad är ditt namn? ")
    return name

def splash():
    print(" _____                               _                                _    _   ") 
    print("|  __ \                             | |                              | |  | |  ")
    print("| |  | |  ___   ___  ___  _ __ ___  | |__    ___  _ __  _ __    __ _ | |_ | |_ ")
    print("| |  | | / _ \ / __|/ _ \| '_ ` _ \ | '_ \  / _ \| '__|| '_ \  / _` || __|| __|")
    print("| |__| ||  __/| (__|  __/| | | | | || |_) ||  __/| |   | | | || (_| || |_ | |_ ")
    print("|_____/  \___| \___|\___||_| |_| |_||_.__/  \___||_|   |_| |_| \__,_| \__| \__|")

def choosePath():
    path = ""
    while path != "vänster" and path != "höger" and path != "bakåt" and path != "framåt":
        path = input("Vilken väg väljer du? (framåt, bakåt, höger eller vänster): ")

    return path
        
 

def Rörelse():
    sleep(1)
    print ("Du går ", path)


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
class Hero:
    health = 10
    attack_Damage = 1
    armor = 3

    def take_damage(self,damage):
        self.health -= damage
        return self.health
    def options(self):
        print(f"1) Attack \n2) heal \n3) run")
    def check_dead(self):
        if self.health <=0:
            clear()
            print("GAME OVER NOOBA")
            exit()

class Foes:
    health = 10
    attack_Damage = 5
    armor = 3

    def take_damage(self,damage):
        self.health -= damage
        return self.health

    
def combat_hud(char):
    print(" __________________")
    print(f"| Health Points: {char.health}| \n| Attack Damage: {char.attack_Damage} | \n| Jacket Armor: {char.armor}  | ")
    print("|__________________|")

def combat(hero,enemy):
    val = ""

    while enemy.health > 0:
        combat_hud(hero)
        combat_hud(enemy)
        hero.options()
        val = input("Choose action: ")
        if val == "1":
            if randint(0,1) == 1:
                enemy.take_damage(2*hero.attack_Damage)
            else:
                enemy.take_damage(hero.attack_Damage)
        ### Enemies time to hit back (can fix so it can do special attacks if time is left over.
        if randint(1,3) == 3:
            hero.take_damage(enemy.attack_Damage*2)
        else:
            hero.take_damage(enemy.attack_Damage)
        hero.check_dead()
            
        clear()
    print(f"You won the fight! holy poggers")
#name()
#path = choosePath()
#Rörelse()
#print (splash()) 
#print ("Välkommen till Decembernatt", name())

huvud_karaktär = Hero()
monster = Foes()

combat(huvud_karaktär,monster)

    






 














 












