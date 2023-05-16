from connessione import *
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def extract(message,command):
    message=message.replace(" ","")
    message=message.replace(command,"")
    return message

