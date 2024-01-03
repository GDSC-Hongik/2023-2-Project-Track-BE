# Generated by Django 4.0 on 2024-01-03 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('star', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
