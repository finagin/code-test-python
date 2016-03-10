from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Room, ObjectInRoom

import os


# Create your views here.
def index(request):
    roomId = request.session.get('room', int(os.environ.get('ROOM', '1')))

    return HttpResponseRedirect('/room/' + str(roomId))


def room(request, room_id):
    request.session['room'] = room_id

    room = Room.objects.get(id=room_id)

    sub_rooms = room.relation.all().order_by('id')

    objects = ObjectInRoom.objects.filter(room=room_id).order_by('id')

    a = request.session.get('user_objects', [])

    user_objects = ObjectInRoom.objects.filter(id__in=a).order_by('id')

    return render(
            request,
            'room.html',
            {
                'room': room,
                'sub_rooms': sub_rooms,
                'objects': objects,
                'user_objects': user_objects
            })


def object_take(request, room_id, object_id):
    current_room_id = request.session.get('room', os.environ.get('ROOM', '1'))
    obj = ObjectInRoom.objects.get(id=object_id, room=room_id)
    a = request.session.get('user_objects', [])

    if obj and current_room_id == room_id:
        obj.room = None
        a.append(object_id)
        obj.save()
        request.session['user_objects'] = a

    return HttpResponseRedirect('/room/' + current_room_id)


def obj_put(request, room_id, object_id):
    current_room_id = request.session.get('room', os.environ.get('ROOM', '1'))
    obj = ObjectInRoom.objects.get(id=object_id, room=None)
    a = request.session.get('user_objects', [])
    bool = obj and current_room_id == room_id

    try:
        a.pop(a.index(object_id))
    except ValueError:
        bool = False

    if bool:
        obj.room = Room.objects.get(id=room_id)
        obj.save()
        request.session['user_objects'] = a

    return HttpResponseRedirect('/room/' + str(current_room_id))


def db(request):
    rooms_count = 5
    objects_count = 5
    rooms = [None] * rooms_count
    roomsRelation = [
        [2, 5],
        [3, 5],
        [5],
        [5],
        [],
    ]

    for i in range(0, rooms_count):
        room = Room()
        rooms[i] = room
        room.save()

    os.environ['ROOM'] = str(rooms[0].id)

    for i in range(0, rooms_count):
        for j in roomsRelation[i]:
            rooms[i].relation.add(rooms[j - 1])

    for i in range(0, rooms_count):
        for j in range(0, objects_count):
            obj = ObjectInRoom()
            obj.room = rooms[i]
            obj.save()

    return render(
            request,
            'db.html',
            {
                'rooms_count': rooms_count,
                'objects_count': objects_count,
                'go_to': rooms[0].id
            })
