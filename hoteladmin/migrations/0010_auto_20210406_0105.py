# Generated by Django 3.1.5 on 2021-04-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteladmin', '0009_auto_20210406_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='conf_code',
            field=models.CharField(max_length=30),
        ),
    ]
