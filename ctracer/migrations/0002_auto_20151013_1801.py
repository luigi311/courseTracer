# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctracer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='courseNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='section',
            field=models.IntegerField(),
        ),
    ]
