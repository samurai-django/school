# Generated by Django 3.0.5 on 2020-05-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0028_register_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='classes',
        ),
    ]