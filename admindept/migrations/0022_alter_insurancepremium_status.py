# Generated by Django 4.2.5 on 2023-10-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0021_insurancepremium_insurancepremiumitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepremium',
            name='Status',
            field=models.CharField(blank=True, default='Pending', max_length=500),
        ),
    ]