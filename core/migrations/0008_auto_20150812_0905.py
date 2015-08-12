# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150812_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='response',
            table=None,
        ),
    ]
