from connessione import *
from threading import Thread
from caricaDati import *
from Rispondi import *
connection = Connessione("localhost","root","","dbtelegram")
threadCarica = Thread(target=aggiorna, args=[connection])
threadRispondi = Thread(target=comunica, args=[connection])
threadRispondi.start()
threadCarica.start()






            
            