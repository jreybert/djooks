# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150402_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='eisbn',
            field=models.CharField(max_length=13, blank=True),
        ),
    ]
