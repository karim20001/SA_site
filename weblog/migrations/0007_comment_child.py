# Generated by Django 3.2.9 on 2021-12-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0006_auto_20211226_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weblog.comment'),
        ),
    ]
