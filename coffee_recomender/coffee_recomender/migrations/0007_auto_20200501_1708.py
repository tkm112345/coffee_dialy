# Generated by Django 3.0.2 on 2020-05-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_recomender', '0006_auto_20200501_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_date',
            field=models.DateTimeField(),
        ),
    ]
