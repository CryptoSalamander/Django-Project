# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20160918_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='buynum',
            field=models.IntegerField(default=0),
        ),
    ]
