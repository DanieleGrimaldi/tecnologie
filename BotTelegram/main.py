from TelegramAPI import *
from metodi import *
from connessione import *

connection = create_db_connection("localhost","root","","dbtelegram")
#execute_query(connection,"SET GLOBAL max_allowed_packet = 268435456;")
#svuotaDB (connection)
#insertImpianti("https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv",connection)
#insertPrezzi("https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv",connection)

token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"

MyTelegram = Telegram(token) 

listaMessaggi = MyTelegram.getUpdates()
if(listaMessaggi):
    for m in listaMessaggi:  
        if(str(Telegram.text(m)).lower().find("ciao")!=-1):
            MyTelegram.sendMessage(Telegram.chatID(m),"ciao anche a te")
else:
    print("nessun messaggio")


            

            