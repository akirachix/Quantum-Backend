# Generated by Django 5.1.1 on 2024-09-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendsms', '0003_farm_sensordata_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='phone_number',
            field=models.CharField(default='default_value', max_length=15),
        ),
    ]
