# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=255)),
                ('product_description', models.CharField(default='', max_length=1000)),
                ('product_price', models.IntegerField(default=0)),
                ('company_name', models.CharField(default='', max_length=255)),
                ('company_country', models.CharField(default='', max_length=255)),
                ('product_bid', models.IntegerField(default=0)),
            ],
        ),
    ]
