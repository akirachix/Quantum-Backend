# Generated by Django 5.1.1 on 2024-09-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Npkreadings',
            fields=[
                ('npk_id', models.IntegerField(primary_key=True, serialize=False)),
                ('farmer_id', models.IntegerField()),
                ('sensor_id', models.IntegerField()),
                ('npk_readings', models.IntegerField()),
                ('recommendation_id', models.IntegerField()),
            ],
        ),
    ]
