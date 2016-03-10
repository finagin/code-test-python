from django.db import models


# Create your models here.
class Greeting(models.Model):
    id = models.AutoField(primary_key=True)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    relation = models.ManyToManyField('self', symmetrical=True)


class ObjectInRoom(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, null=True)
