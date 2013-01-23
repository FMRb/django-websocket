import datetime
import base64
from django.db import models
from django.template.defaultfilters import slugify

class WebsocketaData(models.Model):
	info = models.TextField(blank=True)
	date = models.DateTimeField() 
	def __unicode__(self):
		return self.info
	
	def set_data(self, info):
		self.info = base64.encodestring(data)
	def get_data(self):
		return base64.decodestring(self.info)	
	def save(self, *args, **kwargs):
		''' On save, update timestamps'''
		if not self.id:
			self.date = datetime.datetime.today()
		super(WebsocketaData, self).save(*args, **kwargs)