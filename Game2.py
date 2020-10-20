from random import *
from time import *
from sys import *
from winsound import Beep

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
    sleep (2)
    
    
    


### Slut på intro ###

#Story



def Game_over():
    print("  ██╗  ██╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗██╗  ██╗ ")
    print("  ╚██╗██╔╝╚██╗██╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ╚██╗██╔╝╚██╗██╔╝ ")
    print("   ╚███╔╝  ╚███╔╝     ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝     ╚███╔╝  ╚███╔╝  ")
    print("   ██╔██╗  ██╔██╗     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗     ██╔██╗  ██╔██╗  ")
    print("  ██╔╝ ██╗██╔╝ ██╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    ██╔╝ ██╗██╔╝ ██╗ ")
    print("  ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ")
    Beep(440 ,500)
    Beep(440, 500)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
    Beep(659, 500)
    Beep(659, 500)
    Beep(659, 500)
    Beep(698, 350)
    Beep(523, 150)
    Beep(415, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
                                                                                                                  
                                                                                                  

def Del_1(val_1):
    if val_1 == "höger":
        print("")
        sleep(2)
        print("Du följer trottoaren och kommer fram till en överfrusen ankdam, i ditt berusade tillstånd får du för dig att det är en bra ide att gå ut på isen. ")
        print("")
        sleep(2)
        val_2 = input("Vill du gå ut på isen? (ja/nej): ")
        if val_2 == "ja":
            sleep(2)
            print("")
            print("Isen knakar när du med stappliga steg rör dig ut på isen. Efter ca 3 meter öppnas marken upp under dig och du glider med ett plums ner i det iskalla vattnet.")
            sleep(2)
            print("")
            Game_over()
            return
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

                
def Del_2():
    sleep(2)
    print("")
    print("Du går in i den mörka gränden, en oroskänsla sprider sig i dig som du rör dig framåt.")
    sleep(2)
    print("")
    val_5 = input("Du ser en skugga röra sig i mörkret. Vad gör du? Chansa och spring förbi hotet, stå på dig och möt hotet, eller vänder du om? (framåt/bakåt/stanna): ")
    if val_5 == "framåt":
        print("")
        sleep(2)
        print("Du snubblar till och slår huvudet på gatstenen")
        sleep(4)
        print("")
        Game_over()
        return
    elif val_5 == "bakåt":
        print("")
        sleep(2)
        print("Du springer tillbaks till Nationen")
        val_1 = input ("Till höger har du fortfarande den upplysta trottoaren. Vilket håll vill du gå åt? (höger): ")
        Del_1(val_1)
    elif val_5 == "stanna":
        print("")
        sleep(2)
        print("En tunn figur träder fram ur skuggorna. Figuren tar gestalten av en gammal kvinna.")
        sleep(2)
        print("")
        print("Kvinnan har krokig rygg, hennes skrovliga ansikte tycks olikt det av en människa och huden tycks obeskrivigt torr i det dunkla skenet.")
        sleep(2)
        print("")
        print("Nästan som att den skulle brista vid minsta beröring.")
        sleep(2)
        print("")
        print ("Med en klar och stark röst olikt dina förväntningar tar kvinnan till orda. Hon säger, lös min gåta och ta del av belöningen: ")
        print("")
        svargåta1 = ""
        n=0
        förmångaförsök = False
        while svargåta1 != "n":
            svargåta1 = input("Med vad börjar natten och slutar dagen? Du har 3 försök(_): ")
            n += 1
            if n > 3:
                förmångaförsök = True
                break
        else :
            print("")
            print("Utmärkt unge man! Här är din belöning")
            print("")
            sleep(2)
            print ("Gumman sträcker fram en underlig glasflaska med en klar röd, svagt skimrande vätska inuti. Flaskan är förseglad med en kork som mörknat.")
            print("")
            sleep(2)
            val_6 = input (" Vill du dricka innehållet i flaskan eller inte? (ja/nej): ")
            if val_6 == "ja" :
                print ("")
                #GE 10 HP ALBIN
                print("")
            elif val_6 == "nej" :
                print ("Du litar inte på innehållet och slänger flaskan i första bästa soptunna.")
                print("")
                sleep(2)
                        
        if förmångaförsök == True :
            print("Bättre lycka nästa gång! Svaret var n!")
            print("")
            sleep(2)
        print ("Den underliga figuren ger dig en sista blick innan du försvinner bort runt nästa huskrök. Du går nu på en gata som leder dig bort mot din lägenhet.")
        print("")
        sleep(2)
        val_7= input("Vill du fortsätta framåt? (ja/nej): ")
        if val_7 == "ja":
            print("")
            sleep(2)
            print("Snyggt! Smart beslut! Du ville ju gå hem!")
        elif val_7 == "nej":
            print("")
            sleep(2)
            print("Varför inte? Du ville ju gå hem! Du går hemåt ändå...")
            print("Mot dig på trottoaren kommer en annan student! Hon har på sig en vikt hatt i papper och ser ut att vara i din ålder, hon kollar lurigt på dig.")
            print("")
            sleep(2)
            print("Hon brister ut, Jahaja, en spexkrigare från", nation, "nation!")
            print("")
            sleep(2)
            if nation in{"norrlands", "kalmars", "stockholms", "västmalands"}: 
                print("Men vi är ju från samma nation! WOW! Lycka till på vägen hem. Tjejen ger dig ett lock till en soptunna med ett handtag på toppen")
                print("")
                sleep(2)
                print("Soptunnelocket liknar en sköld och du känner dig plötsligt starkare.")
                #Ge lite Armour Albin
            else :
                val_8 = input("vad sägs om en Spexstrid? (ja/nej): ")
                if val_8 == "ja" :
                    print("")
                    sleep(2)
                    print ("abc")
                    #Do strid against spexkrigare
                elif val_8 == "nej" :
                    print("")
                    sleep(2)
                    print ("Spexkrigaren från den andra nationen kollar stint på dig, men låter dig passera till slut.")
        
            print("Du går fundersamt gatan fram och funderar på det skumma mötet med studenten.")
        
        
def kapitel_2():    
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
     elif val_4 == 

######## Chapter 2


##### chapter 3

                
#Spelkoden börjar

# print("Formatet på spelet är sådant att du endast kommer svara med små bokstäver dvs: RÄTT=abc apa, gris, FEL=ABC, Apa, Gris. DETTA ÄR EN VIKTIG ASPEKT AV SPELET!")
# print("Ofta ges tips på vad svaret borde vara i en ruta med formatet (svar1/svar2) ibland kommer vi vilja ha ett input från dig.")
# print("Det kan se ut såhär: skriv ditt namn (______ efternamn) svaret skall då vara ditt namn, tillexempel, tomas med små bokstäver!")
# print("")
# sleep(6)
username = input("Vad är ditt namn: ")
print("")
print ("Välkommen",username)
print("")
nation = input("Vilken Studentnation vill du spela för ( _____ nation) ")
print("")
print (nation)
print("")
startgame = input("Starta Spelet? (ja/nej) ")
#if startgame == "ja":
#  print (Intro_prolog())  
    
#else:
#    print ("OK, Bye")

                
val_1 = input ("Till höger ser du en upplyst trottoar, och rakt fram en mörk gränd. Vilket håll vill du gå åt? (framåt/höger): ")
if val_1 == "höger":
    Del_1(val_1)
    
elif val_1 == "framåt":
    Del_2()



#DO STRID AGAINST Råtta





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




 














 












