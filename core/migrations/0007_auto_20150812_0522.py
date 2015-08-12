# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150812_0310'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='response',
            table='core_response',
        ),
    ]
