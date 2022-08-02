# Generated by Django 4.0.5 on 2022-08-01 22:02

import core.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', core.fields.UniqueCharField(max_length=25, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
