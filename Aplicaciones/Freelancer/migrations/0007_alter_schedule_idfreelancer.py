# Generated by Django 4.2.4 on 2023-09-14 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancer', '0006_remove_freelancer_idcity_freelancer_idcity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='idfreelancer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Freelancer.freelancer'),
        ),
    ]