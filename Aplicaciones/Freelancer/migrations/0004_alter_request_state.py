# Generated by Django 4.2.1 on 2023-10-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0003_alter_customer_idcustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='state',
            field=models.CharField(default='Pendiente', max_length=100),
        ),
    ]