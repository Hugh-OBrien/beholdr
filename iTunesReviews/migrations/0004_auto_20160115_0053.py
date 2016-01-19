# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTunesReviews', '0003_auto_20160114_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewreport',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reviewreport',
            name='book',
            field=models.FilePathField(path=b'tempXls'),
        ),
    ]
