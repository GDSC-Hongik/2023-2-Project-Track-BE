# Generated by Django 3.2.23 on 2023-11-21 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0005_review_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coplate.user'),
            preserve_default=False,
        ),
    ]
