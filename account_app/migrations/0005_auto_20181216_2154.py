# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-16 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_auto_20181216_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='account',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='addition',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='bank',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='fax',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='tel',
            field=models.CharField(default='', max_length=20),
        ),
    ]