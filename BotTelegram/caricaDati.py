from connessione import *
from metodi import *
from datetime import datetime
import time
import requests

def aggiorna(connection):
    
    while True:

        now = datetime.now()

        if now.hour==9:#9 per essere sicuri al 100%
            svuotaDB(connection)
            insertImpianti("https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv",connection)
            insertPrezzi("https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv",connection)
            time.sleep(86400000)#sto fermo 1 giorno
        

def insertImpianti(URL,connection):
    response = requests.get(URL)
    query="INSERT INTO  autopompa VALUES"
    text = response.content.decode("utf-8")
    cont=0
    primo=True
    for riga in text.split("\n"):
        v=riga.split(";")
        if cont>1 and riga != "":
            if(isfloat(v[8]) and isfloat(v[9])):
                if not primo:
                    query+=f",\n({v[0]},{v[8]},{v[9]},'{v[2]}')"
                else:
                    query+=f"\n({v[0]},{v[8]},{str.strip(v[9])},'{v[2]}')"     
                    primo=False   
        cont+=1
    query+=";"
    open("impianti.sql", "w").write(query)
    connection.execute_query(query)


def insertPrezzi(URL,connection):
    response = requests.get(URL)
    text = response.content.decode("utf-8")
    cont=0
    primo=True
    valori=10000
    cont2 =valori
    query=""
    for riga in text.split("\n"):

        if(cont2==valori):
            if query != "":
                connection.execute_query(query)
            query="INSERT IGNORE INTO carburante (tipologia,prezzo,idAutopompa) VALUES " 
            cont2=0
            primo=True

        v=riga.split(";")
        if cont>1 and riga != "" and v[3]=="1":             
            if not primo: 
                query+=f","
            query+=f"('{tipologiaCarbrurante(v[1])}',{v[2]},{v[0]})"
            primo = False    

    
        cont2+=1
        cont+=1

    query+=";"
    open("prezzi.sql", "w").write(query)
    connection.execute_query(query)

def svuotaDB (connection):
    sql="TRUNCATE TABLE carburante;"
    connection.execute_query(sql)
    sql="SET FOREIGN_KEY_CHECKS = 0;"
    connection.execute_query(sql)
    sql="TRUNCATE table autopompa"
    connection.execute_query(sql)
    sql="SET FOREIGN_KEY_CHECKS = 1;"
    connection.execute_query(sql)


def tipologiaCarbrurante(type):
    myType = str(type.upper())
    BENZINA = ['BENZINA', 'BLUE SUPER', 'HIQ PERFORM+', 'BENZINA WR 100', 'BENZINA PLUS 98', 'BENZINA SPECIALE', 'F101', 'BENZINA ENERGY 98 OTTANI', 'F-101', 'VERDE SPECIALE', 'V-POWER', 'BENZINA SHELL V POWER', 'BENZINA 100 OTTANI', 'R100', 'BENZINA 102 OTTANI']
    DIESEL = ['GASOLIO', 'BLUE DIESEL', 'HI-Q DIESEL', 'GASOLIO ALPINO', 'GASOLIO SPECIALE', 'GASOLIO PREMIUM', 'EXCELLIUM DIESEL', 'SUPREME DIESEL', 'GASOLIO ECOPLUS', 'GASOLIO ORO DIESEL', 'GASOLIO GELO', 'BLU DIESEL ALPINO', 'DIESELMAX', 'GP DIESEL', 'DIESEL SHELL V POWER', 'GASOLIO ARTICO', 'HVOLUTION', 'GASOLIO ENERGY D', 'E-DIESEL', 'DIESEL E+10', 'GASOLIO PLUS', 'S-DIESEL', 'V-POWER DIESEL']
    GPL = ['GPL']
    METANO = ['METANO', 'GNL', 'L-GNC']
    if(myType in BENZINA):
        return "BENZINA"
    if(myType in DIESEL):
        return "DIESEL"
    if(myType in GPL):
        return "GPL"
    if(myType in METANO):
        return "METANO"
    return "ALTRO"