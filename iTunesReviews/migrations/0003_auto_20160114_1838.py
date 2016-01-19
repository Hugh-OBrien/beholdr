# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTunesReviews', '0002_auto_20160114_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewreport',
            name='name',
            field=models.TextField(),
        ),
    ]
