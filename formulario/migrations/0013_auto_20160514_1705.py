# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0012_auto_20160514_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='description',
            field=models.TextField(),
        ),
    ]
