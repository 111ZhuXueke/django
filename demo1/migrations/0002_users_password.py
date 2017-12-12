# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
