# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duckname', models.CharField(max_length=255)),
                ('ducklastname', models.CharField(max_length=255)),
                ('duckmail', models.EmailField(max_length=255)),
                ('duckage', models.IntegerField()),
            ],
        ),
    ]
