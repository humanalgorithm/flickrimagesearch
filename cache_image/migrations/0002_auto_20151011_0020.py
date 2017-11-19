# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacheimage',
            name='_data',
            field=models.BinaryField(db_column=b'data', blank=True),
        ),
    ]
