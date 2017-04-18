# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_inventaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Description')),
                ('place_occupe', models.IntegerField(verbose_name='Place requise')),
            ],
        ),
    ]
