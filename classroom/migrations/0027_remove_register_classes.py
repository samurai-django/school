# Generated by Django 3.0.5 on 2020-05-18 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0026_auto_20200518_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='classes',
        ),
    ]
