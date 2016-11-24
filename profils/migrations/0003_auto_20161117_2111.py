# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0002_etudiant_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Particulier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=42)),
                ('prenom', models.CharField(max_length=42)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='photos/')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")),
                ('description', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]