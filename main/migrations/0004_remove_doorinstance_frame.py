# Generated by Django 4.1.5 on 2023-01-12 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_accessories_covering_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doorinstance',
            name='frame',
        ),
    ]
