# Generated by Django 4.1.5 on 2023-01-16 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_doorinstance_closer_alter_doorinstance_mezuzah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorinstance',
            name='closer',
            field=models.BooleanField(default=False, verbose_name='מחזיר שמן'),
        ),
        migrations.AlterField(
            model_name='doorinstance',
            name='mezuzah',
            field=models.BooleanField(default=False, verbose_name='מזוזה'),
        ),
        migrations.AlterField(
            model_name='doortype',
            name='covering_into_width_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='רוחבן', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='רוחבן:'),
        ),
    ]