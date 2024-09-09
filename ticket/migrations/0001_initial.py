# Generated by Django 5.1.1 on 2024-09-09 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking_spot', '0001_initial'),
        ('user_management', '0002_alter_customuser_address_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=100, unique=True)),
                ('entry_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('license_plate', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parking_spot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_spot.parkingspot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.customuser')),
            ],
        ),
    ]
