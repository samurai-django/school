# Generated by Django 3.0.5 on 2020-05-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_messagetostudent_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
