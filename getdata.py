import requests
import time
import json
print("#########################################################")
print("######   welcome to my my   #############################")
print("######   piece of shit code #############################")
print("######   its shit but it    #############################")
print("######   works lol oh and   #############################")
print("######   RobbieW made it    #############################")
print("######   this only grabs    #############################")
print("######   shit and  you need something else to parse it lol")
print("#########################################################")
apiKey = input("enter api code here: ")
x = 1
for i in range(0, 115): #I capped it at 115 so even if it breaks the api will not fuck you over
    #lmao some pieces are in dutch but this gets the price
    prijs = (requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey).json()["products"]["RECOMBOBULATOR_3000"]["quick_status"]["buyPrice"])
    #this opens the file i am using a txt file cuz thats what i had open atm json could work but i can't be bothered lol maybe in v2
    f = open("data.txt","a+")
    #this writes the price and some fancy shit to the file
    f.write(f'{x} {prijs} \n')
    # I think you can guess what f.close does if not i'm sorry for you lol
    f.close
    # guess what, this prints the price out
    print(prijs)
    # loop shit
    i = i ++ 1
    x = x ++ 1
    #trying not to get banned from api
    time.sleep(60)
#finishes loop and thats it
print("115 requests we done lol")
