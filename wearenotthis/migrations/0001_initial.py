# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('support_snippet', models.TextField()),
                ('support_long', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
    ]
