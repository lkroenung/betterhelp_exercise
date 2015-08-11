# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('answer_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(serialize=False, primary_key=True)),
                ('question_type', models.CharField(max_length=20)),
                ('question_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('reponse_id', models.IntegerField(serialize=False, primary_key=True)),
                ('answer_id', models.ForeignKey(to='core.Answer')),
                ('question_id', models.ForeignKey(to='core.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.IntegerField(serialize=False, primary_key=True)),
                ('survey_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey_id',
            field=models.ForeignKey(to='core.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(to='core.Question'),
        ),
    ]
