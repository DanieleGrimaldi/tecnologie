import requests

class Telegram:

    def __init__(self, token):
        self.token = token
        self.URL=URL=f"https://api.telegram.org/bot{token}/"

    def getUpdates(self):
        result=requests.post(self.URL+"getUpdates")
        if result.status_code==200:
            dato=result.json()
            if dato["ok"]:
                try:
                    requests.post(self.URL+"getUpdates",params={"offset": dato["result"][-1]["update_id"]+1})
                    return [m["message"] for m in dato["result"]]
                except:
                    return False
        return False
    
    def sendMessage(self,chatID,messaggio="ciao"):
        requests.get(self.URL+"sendMessage",params={"chat_id":chatID,"text":messaggio})
        return True

    def sendPosition(self,chat_id, latitude, longitude):
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        requests.get(self.URL+"sendLocation", params=params)





