# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.CharField(unique=True, max_length=10)),
                ('eisbn', models.CharField(unique=True, max_length=13)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('edition', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to=b'covers')),
            ],
        ),
        migrations.CreateModel(
            name='Book_copy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_date', models.DateTimeField(verbose_name=b'date published')),
                ('book', models.ForeignKey(to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrow_date', models.DateTimeField(verbose_name=b'date published')),
                ('book_copy', models.ForeignKey(to='books.Book_copy')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='borrowing',
            name='borrower',
            field=models.ForeignKey(to='books.User'),
        ),
        migrations.AddField(
            model_name='book_copy',
            name='owner',
            field=models.ForeignKey(to='books.User'),
        ),
    ]
