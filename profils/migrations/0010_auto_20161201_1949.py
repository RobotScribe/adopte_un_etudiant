# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0009_auto_20161124_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='message_postulant',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='postulant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='etudiant',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
