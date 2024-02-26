# Generated by Django 5.0.2 on 2024-02-26 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_reviews', '0002_comment_tourist_spot'),
        ('tourist_attractions', '0004_remove_touristspot_comment_touristspot_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristspot',
            name='comment',
        ),
        migrations.AddField(
            model_name='touristspot',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments_reviews.comment'),
        ),
    ]