# Generated by Django 3.2.23 on 2023-11-12 14:02

import django.core.validators
from django.db import migrations, models
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.'), posts.validators.validate_symbols]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'unique': '이미 있는 제목이네요!'}, max_length=50, unique=True),
        ),
    ]