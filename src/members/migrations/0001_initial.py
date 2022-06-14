# Generated by Django 4.0.5 on 2022-06-14 21:59

import core.fields
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('member_name', core.fields.UniqueCharField(max_length=20, unique=True)),
                ('first_name', core.fields.MandatoryCharField(max_length=50)),
                ('last_name', core.fields.MandatoryCharField(max_length=75)),
                ('email', core.fields.UniqueEmailField(max_length=254, unique=True)),
                ('created_at', core.fields.DefaultFieldNow(default=django.utils.timezone.now)),
                ('active', core.fields.DefaultFieldTrue(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]