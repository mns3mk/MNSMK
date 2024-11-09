import websocket
import ssl
import os
import json
import gzip
import time
from time import sleep
import random
import concurrent.futures
import telebot
created=0
failed=0


L = '\033[1;33m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
X = '\037' 
G = '\033[1;32m'
R = '\033[1;31m'
id = "761058551"

token = "7517539122:AAFgeaW09EkEFh3fj6JUCJ0sjVqSlbtYWJg"
bot = telebot.TeleBot(token)


ch='qwertyuioplkjhgfdsazxcvbnm'
def create():
 global created
 global failed
 user=str(random.choice('qwertyuioplkjhgfdsazxcvbnm')[0])+str(''.join(random.choice(ch) for i in range(11)))
 
 tlg = f'''     
`{user}`
   '''
 

 
 headers = {"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"}
 
 
 data0={"action":"Register","subaction":"Desktop","locale":"en_GB","gmt":"+03","password":{"m1x":"7b04e83921d39450d82327792dbbf5d574785fe3d62b676de4111f5371fba237","m1y":"c7865524cefe571a48fd340a0c0518fe2547d0a9b86631fa6096c36dadc8dc7b","m2":"baefcf8122c389449f9becfc716e8362ea6e416a53fe1204c7fea5ca0d7214bf","iv":"47b034d9d06e9286f422ef09e8c4496b","message":"346921ace2270f72e09f0fded31273632571eee461314e7dea292daf2a7de9224fe4ed506df066089297c91dfb6c40d9a15856794af1fa90db9e42640755b1437fe71ccfec7df2f4dc09e3695dfc7954"},"magicword":{
				"m1x":"4821be439c520d660dbeacb8cd6de5fddf12b80bf1a9e01b2966c604c34086ec","m1y":"7871a3e18f1c5711441bc30710d72d4e9b762d126609fd405e17d41bce580566"
,"m2":"ee5841e1d2bb30120a2f53cd6810c2c56fad1df12090d55a24aaad1b347ad201",
"iv":"efe711d355a1d8a80e0b45d93b5d6723","message":"a54c46093395bdca49dbe3758ddac3a6"}
,"magicwordhint":"0000","login":str(user),"devicename":"Samsung SM-A127F","softwareversion":"1.1.0.2300","nickname":None,"os":"AND","deviceuid":"1eb6e1c129e559b4","devicepushuid":"*eYq74iDYToWi4D925ieNfK:APA91bEe9rT5-BYkFAU1y9Pt-AKDCNdHemdIkxA5OtC4rfdTasO55Vwl-YL3AGtdXWG9mZNL6Jr9Asr7t3-Cb8w_Oh5loGL3_OAZ5Ld1gbwOakaqPsDoZGkOYDWmPiw5win24foLaors","osversion":"and_13.0.0","id":"1533703124"}
 
 ws=websocket.create_connection("wss://195.13.182.213/Auth", header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
 ws.send(json.dumps(data0))
 result=ws.recv()
 decoded_data = gzip.decompress(result)
 if '"comment":"Exists"' in str(decoded_data):
  failed+=1
 elif '"status":"Success"' in str(decoded_data):
  created+=1
  with open('SafeUM.txt', 'a') as f:
        f.write(user + ":sdam | TG : \n")

  time.sleep(2)
  bot.send_message(id, text=tlg,parse_mode="Markdown")


 elif '"comment":"Retry"' in str(decoded_data):
  failed+=1
 else:
  print(decoded_data)

def send_results_periodically():
    global created
    global failed

executor=concurrent.futures.ThreadPoolExecutor(max_workers=250)
executor.submit(send_results_periodically)


while True:
 executor.submit(create)
 os.system('clear')
 print(C+"safeUm app ")
 print(G+'Created : '+str(created))
 print(R+'Failed : '+str(failed))
