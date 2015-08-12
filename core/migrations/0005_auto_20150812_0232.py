# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='reponse_group_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='response',
            name='reponse_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
