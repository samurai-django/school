# Generated by Django 3.0.5 on 2020-05-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200517_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]