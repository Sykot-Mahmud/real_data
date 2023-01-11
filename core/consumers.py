from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message1':randint(1,100),'message2':randint(100,200),'message3':randint(200,300),'message4':randint(300,400),'message5':randint(400,500),'message6':randint(500,600)}))

            sleep(1)
