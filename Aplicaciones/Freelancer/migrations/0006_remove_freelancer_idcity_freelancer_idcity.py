# Generated by Django 4.2.4 on 2023-09-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0005_service_remove_schedule_title_schedule_idfreelancer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='idcity',
        ),
        migrations.AddField(
            model_name='freelancer',
            name='idcity',
            field=models.ManyToManyField(to='Freelancer.city'),
        ),
    ]