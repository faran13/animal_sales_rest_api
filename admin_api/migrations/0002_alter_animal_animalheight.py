# Generated by Django 4.0 on 2021-12-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animalHeight',
            field=models.IntegerField(),
        ),
    ]