# Generated by Django 4.0.5 on 2022-07-26 21:00

import core.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', core.fields.UniqueCharField(max_length=30, unique=True)),
                ('slug', core.fields.UniqueCharField(max_length=30, unique=True)),
                ('description', core.fields.MandatoryCharField(max_length=150)),
                ('about', core.fields.MandatoryTextField()),
                ('members', models.ManyToManyField(to='members.member')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
