# Generated by Django 4.1.5 on 2023-01-12 09:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_doorinstance_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='')),
                ('index', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Covering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='structure',
            name='compatible_doors',
        ),
        migrations.RemoveField(
            model_name='structure',
            name='compatible_engraving',
        ),
        migrations.RemoveField(
            model_name='doorsgroupinstance',
            name='engraving',
        ),
        migrations.RemoveField(
            model_name='order',
            name='casing',
        ),
        migrations.RemoveField(
            model_name='order',
            name='engraving',
        ),
        migrations.AddField(
            model_name='doortype',
            name='binder_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='הפחתה ברוחב', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='הפחתה ברוחב:'),
        ),
        migrations.AddField(
            model_name='doortype',
            name='covering_into_height_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='הפחתה בגובה', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='הפחתה בגובה:'),
        ),
        migrations.AddField(
            model_name='doortype',
            name='covering_into_width_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='הפחתה ברוחב', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='הפחתה ברוחב:'),
        ),
        migrations.AddField(
            model_name='doortype',
            name='covering_out_height_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='הפחתה בגובה', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='הפחתה בגובה:'),
        ),
        migrations.AddField(
            model_name='doortype',
            name='covering_out_width_calculation',
            field=models.DecimalField(decimal_places=1, default=0, help_text='הפחתה ברוחב', max_digits=4, validators=[django.core.validators.MaxValueValidator(0)], verbose_name='הפחתה ברוחב:'),
        ),
        migrations.AddField(
            model_name='hinge',
            name='index',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lock',
            name='index',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EngravingType',
        ),
        migrations.DeleteModel(
            name='Structure',
        ),
        migrations.AddField(
            model_name='covering',
            name='compatible_doors',
            field=models.ManyToManyField(blank=True, help_text='דלתות מתאימות', to='main.doortype', verbose_name='סוגי דלתות תואמים:'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='compatible_doors',
            field=models.ManyToManyField(blank=True, help_text='דלתות מתאימות', to='main.doortype', verbose_name='סוגי דלתות תואמים:'),
        ),
    ]
