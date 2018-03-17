# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_item_buynum'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='parcelnum',
            field=models.IntegerField(default=0),
        ),
    ]
