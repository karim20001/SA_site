# Generated by Django 3.2.9 on 2022-01-05 07:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0011_auto_20211228_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='child',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='some', to='weblog.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 7, 59, 40, 482352, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 7, 59, 40, 482352, tzinfo=utc)),
        ),
    ]
