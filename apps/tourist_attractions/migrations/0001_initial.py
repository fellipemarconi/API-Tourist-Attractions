# Generated by Django 5.0.2 on 2024-02-23 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '__first__'),
        ('attractions', '__first__'),
        ('comments_reviews', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=4000)),
                ('is_approved', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, upload_to='tourist-attractions/%Y/%m/')),
                ('address', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='address.address')),
                ('attractions', models.ManyToManyField(default='', to='attractions.attraction')),
                ('comment', models.ManyToManyField(default='', to='comments_reviews.comment')),
            ],
            options={
                'verbose_name': 'Tourist Spot',
                'verbose_name_plural': 'Tourist Spots',
            },
        ),
    ]
