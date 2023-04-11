from prezzi import *

def leggiPrezzi(nomeFile):
    file = open(nomeFile, "r")
    cont=0
    ListaPrezzi=[]
    for riga in file.readlines():
        if cont>1:
            v=riga.split(";")
            #print(str.strip(v[4]))
            temp=prezzi(v[0],v[1],v[2],v[3],str.strip(v[4]))
            ListaPrezzi.insert(cont,temp)
        cont+=1
    return ListaPrezzi
