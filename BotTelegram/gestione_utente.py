from connessione import *

def start(chatID,username,connection):
    sql=f"select * from utente where IDchat = '{chatID}'"
    result=connection.read_query(sql)
    if len(result)>0:
        return result[0][0]
    else:
        sql=f"INSERT INTO utente (IDchat,username) VALUES ({chatID},'{username}');"
        connection.execute_query(sql)
        sql=f"select * from utente where IDchat = '{chatID}'"
        result=connection.read_query(sql)
        return result[0][0]

def setCapienza(chatID,capienza,connection):
    if capienza.isnumeric() and capienza>5 and capienza<200:
        sql=f"UPDATE utente SET capienza={capienza} WHERE chatID={chatID}; "
        connection.execute_query(sql)
        return "eseguito con successo"
    else:
        return "manda un dato reale"

    


    