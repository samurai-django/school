# Generated by Django 3.0.5 on 2020-05-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0035_auto_20200519_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]