from TelegramAPI import *
from metodi import *
from connessione import *
from caricaDati import *
from gestione_utente import *
from threading import Thread

connection = Connessione("localhost","root","","dbtelegram")
#threadCarica = Thread(target=aggiorna(connection))
#threadCarica.start()


token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"
MyTelegram = Telegram(token) 

response="non ho capito"

listaMessaggi = MyTelegram.getUpdates()
if(listaMessaggi):
    for m in listaMessaggi:  
        message = str(m["text"]).lower()
        chatID = m["chat"]["id"]
        if(message.find("/start")!=-1):
            myid=start(chatID,m["chat"]["username"],connection)
            MyTelegram.sendMessage(chatID,myid)
            
        if(message.find("/settipologia")!=-1):
            response=setTipologia(chatID,extract(message,"/settipologia"),connection)

        if(message.find("/setcapienza")!=-1):
            response=setCapienza(chatID,extract(message,"/setcapienza"),connection)

        if(message.find("/setconsumo")!=-1):
            response=setConsumo(chatID,extract(message,"/setconsumo"),connection)

        MyTelegram.sendMessage(chatID,response)

        print(issetVar(chatID,connection))

            
else:
    print("nessun messaggio")



            
            