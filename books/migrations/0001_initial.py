# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-27 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=150)),
                ('book_name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('book_author', models.CharField(max_length=150)),
                ('publication_year', models.IntegerField(default=0)),
                ('publisher', models.CharField(max_length=150)),
                ('page_count', models.IntegerField(default=0)),
            ],
        ),
    ]
