# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.BooleanField(default=False)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='film',
            name='url',
            field=models.URLField(default=0),
            preserve_default=True,
        ),
    ]
