from socketio import socketio_manage

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect

#Include the models of the database to save the files.
#Database sqlite3 saving the data in the file wensocketa.db
from websocketa.models import WebsocketaData
from websocketa.websocketa_socketio import WebsocketaNamespace

def base(request, template='base.html'):
	context={}
	return render(request, template, context)

def update(request , template="update.html"):
	"""
		Handle the process of update the files ?
	"""
	#text = request.POST.get("infoarea")
	#if text:
	#	newdata=WebsocketaData(_info=text)
	#	newdata.save()
	context = {"files": WebsocketaData.objects.all()}
	return render(request, template, context)