# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20160918_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pwdchk',
        ),
    ]
