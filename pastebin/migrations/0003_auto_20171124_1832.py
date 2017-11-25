# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0002_auto_20171124_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='syntax',
            field=models.IntegerField(choices=[('plain', 'Plain'), ('python', 'Python'), ('html', 'HTML'), ('sql', 'SQL'), ('javascript', 'Javascript'), ('css', 'CSS')], default=0),
        ),
    ]