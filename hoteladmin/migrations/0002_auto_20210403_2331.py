# Generated by Django 3.1.5 on 2021-04-03 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoteladmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='.')),
                ('avail', models.BooleanField(default=True)),
                ('served_at', models.CharField(blank=True, choices=[('BR', 'BreakFast'), ('LN', 'Lunch'), ('DI', 'Dinner')], max_length=2)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('NIN', 'North Indian'), ('IT', 'Italian'), ('CHI', 'Chinese'), ('SIN', 'South Indian'), ('KR', 'Korean'), ('SD', 'Side'), ('DES', 'Dessert'), ('BUR', 'Burger'), ('BEV', 'Beverages'), ('SOU', 'Soup'), ('SAL', 'Salad')], default='DEF', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField(default=0)),
                ('cnf_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('order_status', models.CharField(choices=[('PD', 'Pending'), ('CON', 'Confirm')], default='PD', max_length=3)),
                ('bill_status', models.CharField(choices=[('PD', 'Pending'), ('PD', 'Paid')], default='PD', max_length=3)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('avg_time', models.IntegerField(default=0)),
                ('items', models.ManyToManyField(related_name='_order_items_+', to='hoteladmin.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_code', models.CharField(max_length=10)),
                ('cust_name', models.CharField(max_length=25)),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(default=20)),
                ('takeaway', models.BooleanField(blank=True, default=False)),
                ('payment', models.CharField(choices=[('GPAY', 'Google Pay'), ('UPI', 'UPI PhonePe')], default='Cash', max_length=4)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('date', models.DateField(null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('cuisine', models.CharField(choices=[('MC', 'MultiCuisine Restaurant'), ('VEG', 'Pure Veg')], default='MC', max_length=4)),
                ('status', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], default='CL', max_length=3)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaraunt', to='hoteladmin.address')),
                ('combos', models.ManyToManyField(blank=True, related_name='_restaurant_combos_+', to='hoteladmin.Dish')),
                ('dishes', models.ManyToManyField(blank=True, related_name='restaraunt', to='hoteladmin.Dish')),
                ('orders', models.ManyToManyField(blank=True, related_name='_restaurant_orders_+', to='hoteladmin.Order')),
            ],
        ),
        migrations.DeleteModel(
            name='flight',
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hoteladmin.restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]