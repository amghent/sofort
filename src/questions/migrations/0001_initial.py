# Generated by Django 4.0.5 on 2022-07-26 13:33

import core.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', core.fields.MandatoryTextField()),
                ('created_at', core.fields.DefaultFieldNow(default=django.utils.timezone.now)),
                ('last_updated_at', core.fields.OptionalTimestampField(blank=True, null=True)),
                ('title', core.fields.MandatoryCharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('interest_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.interestgroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', core.fields.MandatoryTextField()),
                ('created_at', core.fields.DefaultFieldNow(default=django.utils.timezone.now)),
                ('last_updated_at', core.fields.OptionalTimestampField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionReply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', core.fields.MandatoryTextField()),
                ('created_at', core.fields.DefaultFieldNow(default=django.utils.timezone.now)),
                ('last_updated_at', core.fields.OptionalTimestampField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('question_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questionanswer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
