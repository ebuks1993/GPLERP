# Generated by Django 4.2.5 on 2023-09-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindept', '0015_alter_premiumpaid_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumpaid',
            name='transaction',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='admindept.admintransaction'),
        ),
    ]
