# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_auto_20180225_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]