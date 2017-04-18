# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='inventaire',
            field=models.ForeignKey(to='inv.Inventaire', null=True),
        ),
        migrations.AlterField(
            model_name='inventaire',
            name='place_max',
            field=models.IntegerField(verbose_name='Place max'),
        ),
    ]
