# Generated by Django 5.0.2 on 2024-02-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_rename_atrraction_attraction'),
        ('tourist_attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='attractions',
            field=models.ManyToManyField(default='', to='attractions.attraction'),
        ),
    ]
