# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_remove_medicamento_hospitalar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sintoma',
            name='nome',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
