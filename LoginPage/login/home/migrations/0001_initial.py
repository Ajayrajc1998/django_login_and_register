# Generated by Django 4.1.5 on 2023-01-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineer_name', models.CharField(max_length=100)),
                ('engineer_role', models.TextField()),
            ],
        ),
    ]