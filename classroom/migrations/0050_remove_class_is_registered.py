# Generated by Django 3.0.5 on 2020-05-21 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0049_class_is_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='is_registered',
        ),
    ]
