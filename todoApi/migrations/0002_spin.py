# Generated by Django 3.2.25 on 2024-06-18 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]