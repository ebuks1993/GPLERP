# Generated by Django 4.2.5 on 2023-09-19 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0006_fullpremium_premiumpaid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullpremium',
            old_name='package',
            new_name='month',
        ),
    ]