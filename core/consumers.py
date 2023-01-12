from channels.generic.websocket import WebsocketConsumer
import json
import  random 
from time import sleep
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message1':round(random.uniform(33.33, 66.66), 2),'message2':round(random.uniform(33.33, 66.66), 2),'message3':round(random.uniform(33.33, 66.66), 2),'message4':round(random.uniform(33.33, 66.66), 2),'message5':round(random.uniform(33.33, 66.66), 2),'message6':round(random.uniform(200, 206.66), 2)}))
            
            sleep(1)
