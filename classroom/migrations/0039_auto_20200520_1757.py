# Generated by Django 3.0.5 on 2020-05-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0038_auto_20200520_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='semester',
            field=models.CharField(choices=[('Q1', '1'), ('Q2', '2'), ('Q3', '3'), ('Q4', '4'), ('summer vacation', 'summer vacation'), ('winter vacation', 'winter vacation')], default=False, max_length=20),
        ),
    ]