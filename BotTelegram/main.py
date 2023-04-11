from TelegramAPI import *
from prezzi import *
from metodi import *

myPrezzi = leggiPrezzi("prezzo_alle_8.csv")

print(myPrezzi[0])

token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"

MyTelegram = Telegram(token) 

listaMessaggi = MyTelegram.getUpdates()
if(listaMessaggi):
    for m in listaMessaggi:  
        if(str(Telegram.text(m)).lower().find("ciao")!=-1):
            MyTelegram.sendMessage(Telegram.chatID(m),"ciao anche a te")
else:
    print("nessun messaggio")


            

            