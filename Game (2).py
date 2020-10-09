from random import *
from time import *

def name():
    namn=input(" Välkommen, Vad är ditt namn? ")
    return name
name()
def splash():
    print(" _____                               _                                _    _   ") 
    print("|  __ \                             | |                              | |  | |  ")
    print("| |  | |  ___   ___  ___  _ __ ___  | |__    ___  _ __  _ __    __ _ | |_ | |_ ")
    print("| |  | | / _ \ / __|/ _ \| '_ ` _ \ | '_ \  / _ \| '__|| '_ \  / _` || __|| __|")
    print("| |__| ||  __/| (__|  __/| | | | | || |_) ||  __/| |   | | | || (_| || |_ | |_ ")
    print("|_____/  \___| \___|\___||_| |_| |_||_.__/  \___||_|   |_| |_| \__,_| \__| \__|")

print (splash()) 
print ("Välkommen till Decembernatt", name())

def choosePath():
    path = ""
    while path != "vänster" and path != "höger" and path != "bakåt" and path != "framåt":
        path = input("Vilken väg väljer du? (framåt, bakåt, höger eller vänster): ")

    return path
        
path = choosePath() 

def Rörelse():
    sleep(1)
    print ("Du går ", path)
    
    
Rörelse()



 












