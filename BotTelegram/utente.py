from connessione import *
class utente:

    def __init__(self,chatID,connection):
        sql=f"select from utente where IDchat = '{chatID}'"
        result=connection.read_query(sql)
        
         



    