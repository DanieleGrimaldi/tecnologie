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
    capienza=int(capienza)
    if  capienza>=5 and capienza<=200:
        sql=f"UPDATE utente SET capienza={capienza} WHERE chatID={chatID}; "
        connection.execute_query(sql)
        return "eseguito con successo"
    else:
        return "manda un dato reale min 5 max 200"
    
def setTipologia(chatID,tipologia,connection):

    if str(tipologia).upper() in ["BENZINA","DIESEL","GPL","METANO"]:
        sql=f"UPDATE utente SET tipologia='{tipologia}' WHERE chatID={chatID}; "
        connection.execute_query(sql)
        return "eseguito con successo"
    else:
        return "scegli tra benzina diesel gpl e metano"
    
def setConsumo(chatID,consumo,connection):
    consumo=int(consumo)
    if consumo>=5 and consumo<=30:
        sql=f"UPDATE utente SET consumo={consumo} WHERE chatID={chatID}; "
        connection.execute_query(sql)
        return "eseguito con successo"
    else:
        return "manda un dato reale max 30 min 5"
    
def issetVar(chatID,connection):

    sql=f"select * from utente where chatID = '{chatID}';"
    result=connection.read_query(sql)
    if len(result)>0:
        for var in result[0]:
            if var == "" or var == 0:
                return False
    return True

def dati(chatID,connection):
    sql=f"select tipologia,consumo,capienza from utente where chatID = '{chatID}'"
    result=connection.read_query(sql)
    return result[0]

def ricerca(chatID,connection,latitude,longitude):
    if(not issetVar(chatID,connection)):
        return "devi prima inserire i dati"
    else:
        conveniente=0
        spesaMin=100000000
        utente=dati(880180377,connection)
        tipo=utente[0]
        sql=f'''SELECT latitude,longitude,catena,prezzo,
                    (6371000 * Acos (Cos (Radians({latitude})) * Cos(Radians(latitude)) *
                                        Cos(Radians(longitude) - Radians({longitude}))
                                        + Sin (Radians({latitude})) *
                                            Sin(Radians(latitude)))
                    ) AS distance_m
                FROM   autopompa join carburante on autopompa.id=carburante.idAutopompa
                where tipologia="{tipo}"
                ORDER  BY distance_m 
                LIMIT  20;'''
        result=connection.read_query(sql)
        for var in result:
            spesa=costoEffettivo(utente[1],var[3],var[4]/1000,utente[2])
            if(spesa<spesaMin):
                spesaMin=spesa
                conveniente=var

        return conveniente

def costoEffettivo(consumo,prezzo,distanza,quantita):
    lkm=1/consumo
    spesa=quantita*prezzo
    spesa+=(distanza*2)*lkm*prezzo
    return spesa












    