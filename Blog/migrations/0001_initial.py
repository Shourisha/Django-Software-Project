# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-07 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Body', models.CharField(max_length=500)),
            ],
        ),
    ]
