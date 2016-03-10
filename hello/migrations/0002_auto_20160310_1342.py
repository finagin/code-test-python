# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectInRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('relation', models.ManyToManyField(related_name='_room_relation_+', to='hello.Room')),
            ],
        ),
        migrations.RemoveField(
            model_name='greeting',
            name='when',
        ),
        migrations.AlterField(
            model_name='greeting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='objectinroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Room'),
        ),
    ]