# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='realisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('projet', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
