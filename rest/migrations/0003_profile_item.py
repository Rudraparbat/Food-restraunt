# Generated by Django 5.0.7 on 2024-07-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='item',
            field=models.ManyToManyField(blank='False', to='rest.foods'),
        ),
    ]
