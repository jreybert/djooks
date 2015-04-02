# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=b'covers', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='eisbn',
            field=models.CharField(unique=True, max_length=13, blank=True),
        ),
    ]
