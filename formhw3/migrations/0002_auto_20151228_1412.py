# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formhw3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]