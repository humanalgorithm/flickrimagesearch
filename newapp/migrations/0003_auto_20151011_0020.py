# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20151010_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='_data',
            field=models.BinaryField(db_column=b'data', blank=True),
        ),
    ]
