import requests
import time
import json
#removed cringe
apiKey = input("enter api key here: ")
x = 1
for i in range(0, 115): 
    prijs = (requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey).json()["products"]["RECOMBOBULATOR_3000"]["quick_status"]["buyPrice"])
    f = open("data.txt","a+")
    f.write(f'{x} {prijs} \n')
    f.close
    print(prijs)
    i = i ++ 1
    x = x ++ 1
    time.sleep(60)
print("115 requests we done lol")
