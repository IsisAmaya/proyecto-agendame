# Generated by Django 4.2.1 on 2023-10-16 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='requesttime',
            field=models.TimeField(),
        ),
    ]