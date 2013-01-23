import logging

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace

from websocketa.models import WebsocketaData

"""
Definition of the namespace to connect the sockect through socket.io.js
This code is in charge of manage the save of the information and return the confirmation
of receving the information from the client.
"""
@namespace('/update')
class WebsocketaNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):	
	def initialize(self):
		self.logger = logging.getLogger("socketio.websocketa")
		self.log("Socketio session started")
		
	def log(self, message):
		self.logger.info("[{0}] {1}".format(self.socket.sessid, message))
	
	def on_user_send(self, data):
		self.log("se ha recibido")
		#Save the information in the database.
		newdata=WebsocketaData(info=data)
		newdata.save()
		#Send the confirmation message to the client.
		self.broadcast_event('broadcast',' The text has been saved')
		return True