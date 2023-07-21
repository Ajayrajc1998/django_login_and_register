# Generated by Django 4.1.5 on 2023-01-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_about_engineer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('f_post', models.TextField()),
                ('f_image', models.ImageField(upload_to='faculty')),
            ],
        ),
    ]
