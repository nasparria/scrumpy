# Generated by Django 4.0.3 on 2022-06-07 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
    ]
