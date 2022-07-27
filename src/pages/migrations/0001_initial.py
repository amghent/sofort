# Generated by Django 4.0.6 on 2022-07-27 08:01

import core.fields
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', core.fields.UniqueCharField(max_length=250, unique=True)),
                ('slug', core.fields.UniqueCharField(max_length=50, unique=True)),
                ('intro', core.fields.MandatoryTextField()),
                ('content', core.fields.MandatoryTextField()),
                ('show_in_navigation', core.fields.DefaultFieldFalse(default=False)),
                ('show_in_footer', core.fields.DefaultFieldFalse(default=False)),
                ('menu_title', core.fields.OptionalCharField(blank=True, max_length=20, null=True)),
                ('created_at', core.fields.DefaultFieldNow(default=django.utils.timezone.now)),
                ('last_updated_at', core.fields.OptionalTimestampField(blank=True, null=True)),
                ('authors', models.ManyToManyField(to='members.member')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
