# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0004_auto_20170418_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventaire',
            name='proprietaire',
            field=models.OneToOneField(null=True, to='inv.Member'),
        ),
    ]
