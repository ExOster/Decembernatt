from random import *
from time import *

def Intro_prolog():
    print(" _____                               _                                _    _   ") 
    print("|  __ \                             | |                              | |  | |  ")
    print("| |  | |  ___   ___  ___  _ __ ___  | |__    ___  _ __  _ __    __ _ | |_ | |_ ")
    print("| |  | | / _ \ / __|/ _ \| '_ ` _ \ | '_ \  / _ \| '__|| '_ \  / _` || __|| __|")
    print("| |__| ||  __/| (__|  __/| | | | | || |_) ||  __/| |   | | | || (_| || |_ | |_ ")
    print("|_____/  \___| \___|\___||_| |_| |_||_.__/  \___||_|   |_| |_| \__,_| \__| \__|")
    sleep(2)
    print("")
    print("Decembernatt utspelar sig i en alternativ framtid.")
    sleep(2)
    print("Efter det stora prankkriget 2020 som kulminerade i")
    sleep(2)
    print("vattenbombningen av Norrlands Nation har ")
    sleep(2)
    print("studentnationerna legat i konstant spexkrig. Stridigheterna")
    sleep(2)
    print("manifesterar sig igenom gatustrider där studentrepresentanter")
    sleep(2)
    print("från olika nationer spex slåss om rättigheterna att kalla sig den bästa nationen")
    print("")
    sleep(4)
    print("Efter sluttentorna i December bestämmer sig du och några kurskambrater er för att gå ut på Nation.")
    sleep(2)
    print("5 öl, 3 toabesök, och 1 stukad fot senare är det dags att röra sig hemåt.")
    sleep(2)
    print("Du", username,",tar ett par stappligt steg ut i decemberkylan. Ner på den lätt puderbeklädda trottoaren.")
    sleep(2)
    print("Från den mörka natthimlen faller knallvita snöflingor upplysta av fullmånen. Du känner att du vill ta dig hem!")
    sleep(2)
    
    
username = input("Vad är ditt namn: ")
print ("Välkommen ",username)
startgame = input("Starta Spelet? (ja/nej) ")
if startgame == "ja":
  print (Intro_prolog())  
    
else:
    print ("OK, Bye")

### Slut på intro ###

#Story

GO = "XXXX GAME OVER XXXX"
val_1 = input ("Till höger ser du en upplyst trottoar, och rakt fram en mörk gränd. Vilket håll vill du gå åt? (framåt/höger): ")
print("")
if val_1 == "höger":
    print("Du följer trottoaren och kommer fram till en överfrusen ankdam, i ditt berusade tillstånd får du för dig att det är en bra ide att gå ut på isen. ")
    print("")
    sleep(2)
    val_2 = input("Vill du gå ut på isen? (ja/nej): ")
    if val_2 == "ja":
        sleep(2)
        print("")
        print("Isen knakar när du med stappliga steg rör dig ut på isen. Efter ca 3 meter öppnas marken upp under dig och du glider med ett plums ner i det iskalla vattnet.")
        sleep(2)
        print(GO)
    elif val_2 == "nej":
        sleep(2)
        print("")
        print("Du inser att det inte är ett smart beslut att gå ut på isen, speciellt inte i ditt tillstånd. ")
        sleep(2)
        print("")
        print("Du rör dig framåt en bit men stannar kvikt när du ser en anka sittandes på en skateboard intill iskanten. Ankan kollar med en ondsint blick på dig och väser. ")
        sleep(2)
        print("")
        val_3 = input ("Vill du utmana ankan för prospektet att få skateboarden eller tar du höger och går runt ankan? (attack/höger): ")
        if val_3 == "attack":
            sleep(2)
            print("")
            print("ATTACK")
            #DO STRID AGAINST ANKA if förlust=GO VINST=REWARD, REWARD SKATEBOARD? borde sen printa val från "fortsätt här"
        elif val_3 == "höger": #randomise attack ändå?
            sleep(2)
            print("")
            print("Du går över vägen och runt ankan. Han följer dig med blicken men lämnar dig ifred.")
            sleep(2)
        print("Du kommer till en korsning i vägen.") #"fortsätt här"
        print("")
        sleep(2)
        print("Snabbaste vägen hem är att ta den mindre stigen igenom skogen till höger, men den är inte upplyst! Den asfalterande vägen till vänster är större och upplyst men tar längre tid.")
        print("")
        sleep(2)
        val_4 = input("Tar du vänster eller höger? (höger/vänster): ")
        if val_4 == "höger":
            print("")
            sleep(2)
            print("Du tar stigen igenom skogen. Halvvägs igenom skogen ser du 3 personer med ov-ar närma sig.")
            sleep(2)
            print("")
            val_5 = input("Vad gör du? (fly/strid): ")
            if val_5 == "fly":
                sleep(2)
                print ("Du försöker fly men studenterna omringar dig och uppmanar dig att anta utmaningen om spexstrid")
            elif val_5 == "strid" :
                print("strid")
                    #DO STRID AGAINST GOONS    
        
elif val_1 == "framåt":
    print("Du går in i den mörka gränden, en oroskänsla sprider sig i dig som du rör dig framåt.")
    sleep(2)
    val_5 = input("Du ser en skugga röra sig i mörkret. Vad gör du? Chansa och spring förbi hotet, stå på dig och möt hotet, eller vänder du om? (framåt/bakåt/stanna/): ")
    if val_5 == "framåt":
        print("Du snubblar till och slår huvudet på gatstenen")
        print(GO)
    elif val_5 == "bakåt":
        print("Du springer tillbaks till Nationen")
    elif val_5 == "stanna":
        print("123")
#DO STRID AGAINST Råtta










def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
class Hero:
    name = "You"
    max_health = 30
    health = 30
    attack_Damage = 3
    armor = 1
    healing = 10
    
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

class Anka:
    name = "Anka"
    health = 15
    attack_Damage = 2
    armor = 1

    def take_damage(self,damage):
        self.health -= damage
        return self.health
class Student_Goons:
    name = "Student Goons"
    health = 20
    attack_Damage = 3
    armor = 1

    def take_damage(self,damage):
        self.health -= damage
        return self.health

    
def combat_hud(char):
    print(char.name)
    print(" __________________")
    print(f" Health Points: {char.health} \n Attack Damage: {char.attack_Damage}  \n Defense: {char.armor}   ")
    print(" __________________")

def combat(hero,enemy,enemy_prompt):
    val = ""
    clear()
    while enemy.health > 0:
        combat_hud(hero)
        combat_hud(enemy)
        hero.options()
        dmg_taken_hero_calc = 0
        dmg_taken_enemy_calc = 0
        
        val = input("Choose action: ")
        if val == "1":
            if randint(0,1) == 1:
                dmg_taken_enemy_calc = 2*hero.attack_Damage-enemy.armor
                enemy.take_damage(dmg_taken_enemy_calc)
            else:
                dmg_taken_enemy_calc = hero.attack_Damage-enemy.armor
                enemy.take_damage(dmg_taken_enemy_calc)
                
        elif val == "2":
            if hero.max_health - hero.health <= hero.healing:
                Healprompt = "Du healar till max hp"
                hero.health = hero.max_health
            else:
                hero.health += hero.healing
                Healprompt = f"du healar upp ditt hp med {hero.healing}"
        ### Enemies time to hit back (can fix so it can do special attacks if time is left over.
        if randint(1,3) == 3:
            dmg_taken_hero_calc = enemy.attack_Damage*2-hero.armor
            hero.take_damage(dmg_taken_hero_calc)
        else:
            dmg_taken_hero_calc = enemy.attack_Damage-hero.armor
            hero.take_damage(dmg_taken_hero_calc)
        hero.check_dead()
            
        clear()
        
        if val =="1":
            print(f"Du anfaller och gör {dmg_taken_enemy_calc} skada!")
        elif val == "2":
            print(Healprompt)
        print(f"\n{enemy_prompt} för {dmg_taken_hero_calc} skada!")
    clear()
    print(f"You won the fight! holy poggers")
#name()
#path = choosePath()
#Rörelse()
#print (splash()) 
#print ("Välkommen till Decembernatt", name())

huvud_karaktär = Hero()
anka1 = Anka()
student_goons1 = Student_Goons()

combat(huvud_karaktär,anka1,"Ankan biter dig på smalbenet!")

combat(huvud_karaktär,student_goons1,"Studenterna hoppar på dig")


    
