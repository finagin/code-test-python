from django.conf.urls import url

from hello.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^room/(?P<room_id>\d+)$', room, name='room'),
    url(r'^room/(?P<room_id>\d+)/object/(?P<object_id>\d+)/take$', object_take, name='object_take'),
    url(r'^room/(?P<room_id>\d+)/object/(?P<object_id>\d+)/put', obj_put, name='object_put'),
    url(r'^db', db, name='db'),
]
