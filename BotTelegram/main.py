from TelegramAPI import *
from metodi import *
from connessione import *
from caricaDati import *
from threading import Thread

connection = Connessione("localhost","root","","dbtelegram")
threadCarica = Thread(target=aggiorna(connection))
threadCarica.start()


token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"

MyTelegram = Telegram(token) 

listaMessaggi = MyTelegram.getUpdates()
if(listaMessaggi):
    for m in listaMessaggi:  
        if(str(Telegram.text(m)).lower().find("/start")!=-1):
            MyTelegram.sendMessage(Telegram.chatID(m),"ciao anche a te")
else:
    print("nessun messaggio")


            

            