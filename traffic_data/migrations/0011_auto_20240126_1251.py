# Generated by Django 3.2.6 on 2024-01-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_data', '0010_auto_20240126_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficdata',
            name='sizev4',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='trafficdata',
            name='sizev6',
            field=models.BigIntegerField(),
        ),
    ]
