# Generated by Django 3.0.5 on 2020-05-19 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0036_register_is_registered'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Subject',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='tags',
            new_name='subjects',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='tag',
            new_name='subject',
        ),
    ]
