# Generated by Django 4.2.5 on 2023-09-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0018_alter_premiumpaid_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumpaid',
            name='vendor',
            field=models.CharField(null=True),
        ),
    ]