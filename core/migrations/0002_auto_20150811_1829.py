# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='survey_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
