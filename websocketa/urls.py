from django.conf.urls.defaults import patterns, include, url
import socketio.sdjango

urlpatterns = patterns("websocketa.views",
	url("^socket\.io", include(socketio.sdjango.urls)),
	url("^$","base",name="base"),
	url("^update/$","update",name="update"),

)