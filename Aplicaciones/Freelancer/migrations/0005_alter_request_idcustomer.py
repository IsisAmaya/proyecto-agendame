# Generated by Django 4.2.1 on 2023-10-17 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0004_alter_request_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='idcustomer',
            field=models.ForeignKey(default='smartinez', on_delete=django.db.models.deletion.CASCADE, to='Freelancer.customer'),
        ),
    ]