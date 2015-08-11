# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150811_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=b'Question text.', max_length=200),
        ),
    ]
