# Generated by Django 3.0.2 on 2020-03-22 02:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_recomender', '0003_auto_20200322_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='evaluation',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
