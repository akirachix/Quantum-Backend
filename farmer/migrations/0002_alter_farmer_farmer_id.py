# Generated by Django 5.1.1 on 2024-09-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmer",
            name="farmer_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
