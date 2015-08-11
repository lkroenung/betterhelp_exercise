# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150811_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
