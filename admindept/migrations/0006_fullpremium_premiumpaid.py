# Generated by Django 4.2.5 on 2023-09-19 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0005_remove_car_stoke'),
    ]

    operations = [
        migrations.CreateModel(
            name='fullpremium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('refernce', models.CharField(max_length=500, unique=True)),
                ('Amount', models.IntegerField()),
                ('insurance', models.CharField(max_length=500)),
                ('package', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='premiumpaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullpremium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admindept.fullpremium')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admindept.insurance')),
            ],
        ),
    ]