# Generated by Django 4.2.5 on 2023-11-05 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0026_remove_localpaper_car_delete_carpaperpayment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='localpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlateNumber', models.CharField(max_length=20, null=True, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('Car', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admindept.car')),
            ],
        ),
    ]
