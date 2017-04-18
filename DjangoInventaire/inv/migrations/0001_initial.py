# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import inv.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('avatar', models.ImageField(validators=[inv.models.validate_image], blank=True, null=True, verbose_name='Avatar membre', upload_to=inv.models.avatar_filename)),
                ('user', models.OneToOneField(related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
