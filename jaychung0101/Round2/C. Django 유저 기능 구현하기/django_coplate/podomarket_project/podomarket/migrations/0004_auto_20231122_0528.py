# Generated by Django 3.2.23 on 2023-11-22 05:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_auto_20231122_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
