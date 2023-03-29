import requests

token="6104350976:AAHJm-vI7p_gYKR56AyXRzeJKHAvrfBCdgo"
URL=f"https://api.telegram.org/bot{token}/"
ricevere="getUpdates"
mandare="sendMessage"


result=requests.post(URL+ricevere)


if result.status_code==200:
    dato=result.json()
    if dato["ok"]:
        listaMessaggi=[m["message"] for m in dato["result"]]
        for m in listaMessaggi:
            if(str(m["text"])).lower().find("ciao") != -1:
                text="ciao"
                chatID=m["chat"]["id"]
                requests.get(URL+mandare,params={"chat_id":chatID,"text":"ciao"})

        result=requests.post(URL+ricevere,params={"offset":dato["result"][-1]["update_id"]+1})


