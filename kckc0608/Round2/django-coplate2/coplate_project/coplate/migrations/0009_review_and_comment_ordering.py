# Generated by Django 2.2 on 2023-11-26 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0008_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-dt_created']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-dt_created']},
        ),
    ]
