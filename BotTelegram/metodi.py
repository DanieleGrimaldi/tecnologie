from connessione import *
import requests

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
    execute_query(connection, query)

def insertPrezzi(URL,connection):
    response = requests.get(URL)
    query="INSERT INTO carburante VALUES"
    text = response.content.decode("utf-8")
    cont=0
    for riga in text.split("\n"):
        v=riga.split(";")
        if cont>1 and riga != "" and v[3]=="1":             
            if cont!=2:  
                query+=f",\n('{v[1]}',{v[2]},{v[0]})"   
            else:
                query+=f"\n('{v[1]}',{v[2]},{v[0]})"     
        
        cont+=1

    query+=";"
    open("prezzi.sql", "w").write(query)
    #execute_query(connection, query)

def svuotaDB (connection):
    sql="TRUNCATE TABLE carburante;"
    execute_query(connection,sql)
    sql="SET FOREIGN_KEY_CHECKS = 0;"
    execute_query(connection,sql)
    sql="TRUNCATE table autopompa"
    execute_query(connection,sql)
    sql="SET FOREIGN_KEY_CHECKS = 1;"
    execute_query(connection,sql)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False