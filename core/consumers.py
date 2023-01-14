from channels.generic.websocket import WebsocketConsumer
import json
import  random 
from time import sleep



"""
Base WebSocket consumer. Provides a general encapsulation for the
WebSocket handling model that other applications can build on.
Variant of WebsocketConsumer that automatically JSON-encodes and decodes messages 
as they come in and go out.
"""
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({
                'apple_open_amount':round(random.uniform(10.50,49.99), 2),
                'apple_high_amount':round(random.uniform(100.90, 199.99), 2),
                'apple_low_amount':round(random.uniform(50.10,99.99), 2),
                'apple_close_amount':round(random.uniform(50.10, 199.99), 2),
                'amazon_open_amount':round(random.uniform(10.50,49.99), 2),
                'amazon_high_amount':round(random.uniform(100.90, 199.99), 2),
                'amazon_low_amount':round(random.uniform(50.10,99.99), 2),
                'amazon_close_amount':round(random.uniform(50.10, 199.99), 2),
                'tesla_open_amount':round(random.uniform(10.50,49.99), 2),
                'tesla_high_amount':round(random.uniform(100.90, 199.99), 2),
                'tesla_low_amount':round(random.uniform(50.10,99.99), 2),
                'tesla_close_amount':round(random.uniform(50.10, 199.99), 2),
                'meta_open_amount':round(random.uniform(10.50,49.99), 2),
                'meta_high_amount':round(random.uniform(100.90, 199.99), 2),
                'meta_low_amount':round(random.uniform(50.10,99.99), 2),
                'meta_close_amount':round(random.uniform(50.10, 199.99), 2),
                'microsoft_open_amount':round(random.uniform(10.50,49.99), 2),
                'microsoft_high_amount':round(random.uniform(100.90, 199.99), 2),
                'microsoft_low_amount':round(random.uniform(50.10,99.99), 2),
                'microsoft_close_amount':round(random.uniform(50.10, 199.99), 2),

                
                }))
            
            sleep(1)
