# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150812_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='reponse_group_id',
            new_name='response_group_id',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='reponse_id',
            new_name='response_id',
        ),
    ]
