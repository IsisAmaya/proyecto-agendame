# Generated by Django 4.2.4 on 2023-10-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0008_alter_schedule_idfreelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='description',
            field=models.TextField(default=''),
        ),
    ]