# Generated by Django 3.0.5 on 2020-05-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0064_auto_20200523_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship2',
            name='is_date',
            field=models.DateField(auto_now_add=True, default='2020-05-24'),
            preserve_default=False,
        ),
    ]
