# Generated by Django 3.0.5 on 2020-05-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0050_remove_class_is_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]