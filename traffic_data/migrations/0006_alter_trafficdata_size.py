# Generated by Django 3.2.6 on 2024-01-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_data', '0005_auto_20240126_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficdata',
            name='size',
            field=models.BigIntegerField(),
        ),
    ]