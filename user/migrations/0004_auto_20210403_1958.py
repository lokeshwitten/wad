# Generated by Django 3.1.5 on 2021-04-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210403_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='_restaurant_orders_+', to='user.Order'),
        ),
    ]
