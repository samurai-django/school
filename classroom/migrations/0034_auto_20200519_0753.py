# Generated by Django 3.0.5 on 2020-05-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0033_auto_20200519_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(default=None, max_length=20, verbose_name='subject'),
        ),
    ]
