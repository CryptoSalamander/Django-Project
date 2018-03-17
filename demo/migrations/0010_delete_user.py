# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_remove_user_pwdchk'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
