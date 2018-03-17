# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('person_number', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=75)),
                ('account_pw', models.CharField(max_length=50)),
            ],
        ),
    ]
