# Generated by Django 5.0.2 on 2024-02-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0004_alter_touristspot_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='tourtist-attractions/%Y/%m/'),
        ),
    ]