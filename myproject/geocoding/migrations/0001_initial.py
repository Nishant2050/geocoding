# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('docfile', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
