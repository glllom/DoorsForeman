# Generated by Django 4.1.5 on 2023-01-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_doorinstance_closer_doorinstance_mezuzah_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorinstance',
            name='closer',
            field=models.BooleanField(verbose_name='מחזיר שמן'),
        ),
        migrations.AlterField(
            model_name='doorinstance',
            name='mezuzah',
            field=models.BooleanField(verbose_name='מזוזה'),
        ),
    ]
