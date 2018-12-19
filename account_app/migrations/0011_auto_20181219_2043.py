# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0010_auto_20181219_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administration',
            name='id',
        ),
        migrations.AlterField(
            model_name='administration',
            name='contractnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account_app.Contract'),
        ),
    ]
