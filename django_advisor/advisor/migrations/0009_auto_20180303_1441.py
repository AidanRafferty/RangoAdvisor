# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0008_auto_20180303_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.Location'),
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisor.UserProfile'),
        ),
    ]