# Generated by Django 4.1.2 on 2023-01-30 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0020_alter_comment_date_added_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 10, 14, 56, 736896, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 10, 14, 56, 733105, tzinfo=datetime.timezone.utc)),
        ),
    ]
