# Generated by Django 5.0 on 2024-09-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Farmer",
            fields=[
                ("farmers_name", models.CharField(max_length=100)),
                ("farmer_location", models.CharField(max_length=20)),
                ("phone_number", models.CharField(max_length=15, unique=True)),
                ("farmer_id", models.IntegerField(primary_key=True, serialize=False)),
                ("sensor_id", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
