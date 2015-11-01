# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('FIRST_NAME', models.CharField(max_length=30)),
                ('LAST_NAME', models.CharField(max_length=30)),
                ('ADRESS_LINE_1', models.CharField(max_length=30)),
                ('ADRESS_LINE_2', models.CharField(max_length=30)),
                ('TOWN_CITY', models.CharField(max_length=30)),
                ('REGION_STATE', models.CharField(max_length=30)),
                ('COUNTRY', models.CharField(max_length=30)),
                ('POST_CODE', models.IntegerField()),
                ('EMAIL_ADRESS', models.EmailField(max_length=75)),
                ('PHONE_NUMBER', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
