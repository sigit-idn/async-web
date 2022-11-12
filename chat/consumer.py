import json

from channels.generic.websocket import WebsocketConsumer # WebsocketConsumer is a class that provides a number of methods that are useful for handling WebSocket connections.


class ChatConsumer(WebsocketConsumer): # ChatConsumer is used to handle WebSocket connections. It inherits from WebsocketConsumer.
	def connect(self):
		self.accept() # accept() is a method that accepts the connection. It must be called before any other methods are called.

	def disconnect(self, close_code):
		pass

	def receive(self, text_data):
		message = json.loads(text_data)['message']
		
		self.send(text_data=json.dumps({"message": message}))
