# Generated by Django 3.0.5 on 2020-05-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0043_class_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='description',
            field=models.TextField(default=None),
        ),
    ]