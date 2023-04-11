from datetime import datetime

class prezzi:
    def __init__(self,idImpianto,descCarburante,prezzo,isSelf,dtComu):
        self.idImpianto=idImpianto
        self.descCarburante=descCarburante
        self.prezzo=prezzo
        self.isSelf=isSelf
        self.dtComu=datetime.strptime(dtComu, '%d/%m/%Y %H:%M:%S')
    
    def __str__(self):
        return self.descCarburante+" "+self.prezzo