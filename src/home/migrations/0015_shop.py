# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_commissioned_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
                ('prix', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
