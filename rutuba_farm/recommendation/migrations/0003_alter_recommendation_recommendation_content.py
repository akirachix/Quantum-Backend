# Generated by Django 5.0.7 on 2024-09-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_rename_recommendations_content_recommendation_recommendation_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation_content',
            field=models.TextField(max_length=250),
        ),
    ]
