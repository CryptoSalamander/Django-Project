# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='pwdchk',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
