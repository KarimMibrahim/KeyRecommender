# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'NAME')),
                ('subject', models.CharField(blank=True, max_length=150, null=True, verbose_name=b'SUBJECT', choices=[(b'GCS', b'General Customer Service'), (b'Suggest', b'Suggestions'), (b'PS', b'Product Support')])),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'EMAIL ADDRESS', blank=True)),
                ('message', models.TextField(null=True, verbose_name=b'MESSAGE', blank=True)),
            ],
        ),
    ]
