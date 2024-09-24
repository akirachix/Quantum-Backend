# Generated by Django 5.0.7 on 2024-09-20 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NpkReading',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_id', models.IntegerField()),
                ('sensor_id', models.IntegerField()),
                ('npk_reading', models.IntegerField()),
                ('recommendation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NpkReading', to='recommendation.recommendation')),
            ],
        ),
    ]
