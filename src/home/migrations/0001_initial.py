# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
        migrations.CreateModel(
            name='commissioned_work',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to='files/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
                ('url', models.URLField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='home_image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='projet',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='realisation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
                ('projet', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(unique=True, max_length=30)),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')),
                ('year', models.IntegerField(null=True)),
                ('prix', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
