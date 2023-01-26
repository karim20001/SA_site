# Generated by Django 3.2.9 on 2021-12-27 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0007_comment_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more', to='weblog.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='some', to='weblog.comment'),
        ),
    ]
