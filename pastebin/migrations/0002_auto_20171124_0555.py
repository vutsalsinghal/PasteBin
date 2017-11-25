# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='syntax',
            field=models.IntegerField(choices=[(0, 'Plain'), (1, 'Python'), (2, 'HTML'), (3, 'SQL'), (4, 'Javascript'), (5, 'CSS')], default=0),
        ),
    ]
