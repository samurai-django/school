# Generated by Django 3.0.5 on 2020-05-18 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_delete_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='options',
        ),
    ]
