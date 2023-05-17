from TelegramAPI import *
from metodi import *
from gestione_utente import *
import time

def comunica(connection):
    token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"
    MyTelegram = Telegram(token) 

    while True:
        response="non ho capito"

        listaMessaggi = MyTelegram.getUpdates()
        if(listaMessaggi):
            for m in listaMessaggi:
                chatID = m["chat"]["id"]  
                try:
                    response=ricerca(chatID,connection,m["location"]["latitude"],m["location"]["longitude"])
                    try:
                        luogo=response[0]
                        MyTelegram.sendPosition(chatID,luogo[0],luogo[1])
                        MyTelegram.sendMessage(chatID,f"{luogo[3]} prezzo al litro\nspesa prevista {round(response[1], 2)}")
                    except:
                        MyTelegram.sendMessage(chatID,response)
                except:
                    try:
                        message = str(m["text"]).lower()

                        if(message.find("/start")!=-1):
                            start(chatID,m["chat"]["username"],connection)
                            response=help()
                        
                        if(message.find("/help")!=-1):
                            response=help()
                            
                        if(message.find("/tipologia")!=-1):
                            response=setTipologia(chatID,extract(message,"/tipologia"),connection)

                        if(message.find("/litri")!=-1):
                            response=setLitri(chatID,extract(message,"/litri"),connection)

                        if(message.find("/consumo")!=-1):
                            response=setConsumo(chatID,extract(message,"/consumo"),connection)
                    
                    except:
                        response="non ho capito"

                    MyTelegram.sendMessage(chatID,response)
        time.sleep(1)