# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('termCode', models.IntegerField()),
                ('termDescr', models.TextField()),
                ('crn', models.IntegerField()),
                ('subj', models.TextField(max_length=2)),
                ('courseNum', models.IntegerField(max_length=3)),
                ('section', models.IntegerField(max_length=3)),
                ('scheduleDesc', models.TextField()),
                ('title', models.TextField()),
                ('maxEnroll', models.IntegerField()),
                ('actEnroll', models.IntegerField()),
            ],
        ),
    ]
