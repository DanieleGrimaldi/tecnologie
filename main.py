from TelegramAPI import *
from metodi import *
from connessione import *
from caricaDati import *
from gestione_utente import *
from threading import Thread

connection = Connessione("localhost","root","","dbtelegram")
#threadCarica = Thread(target=aggiorna, args=connection)
#threadCarica.start()


token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"
MyTelegram = Telegram(token) 

response="non ho capito"

listaMessaggi = MyTelegram.getUpdates()
if(listaMessaggi):
    for m in listaMessaggi:
        chatID = m["chat"]["id"]  
        try:
            response=ricerca(chatID,connection,m["location"]["latitude"],m["location"]["longitude"])
            MyTelegram.sendPosition(chatID,response[0],response[1])

        except:

            message = str(m["text"]).lower()
            if(message.find("/start")!=-1):
                myid=start(chatID,m["chat"]["username"],connection)
                MyTelegram.sendMessage(chatID,myid)
                
            if(message.find("/tipologia")!=-1):
                response=setTipologia(chatID,extract(message,"/tipologia"),connection)

            if(message.find("/capienza")!=-1):
                response=setCapienza(chatID,extract(message,"/capienza"),connection)

            if(message.find("/consumo")!=-1):
                response=setConsumo(chatID,extract(message,"/consumo"),connection)

            MyTelegram.sendMessage(chatID,response)


            
else:
    print("nessun messaggio")



            
            