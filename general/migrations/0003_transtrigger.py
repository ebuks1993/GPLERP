# Generated by Django 4.2.5 on 2023-09-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_customer_department_product_suppplier_team_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='transtrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('approval_status', models.CharField(max_length=500, null=True)),
                ('idenitier', models.CharField(max_length=500)),
                ('Amount', models.IntegerField()),
                ('tabname', models.CharField(max_length=5000)),
            ],
        ),
    ]