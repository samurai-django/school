# Generated by Django 3.0.5 on 2020-05-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_remove_register_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='options',
            field=models.ManyToManyField(to='classroom.Class'),
        ),
    ]
