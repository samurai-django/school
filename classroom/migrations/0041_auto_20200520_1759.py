# Generated by Django 3.0.5 on 2020-05-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0040_auto_20200520_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='grades',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=False),
        ),
    ]
