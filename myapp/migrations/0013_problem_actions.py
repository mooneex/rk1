# Generated by Django 3.2.16 on 2023-09-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20230927_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actions',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]