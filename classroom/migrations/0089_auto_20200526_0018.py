# Generated by Django 3.0.5 on 2020-05-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0088_auto_20200526_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourse',
            name='course',
            field=models.ManyToManyField(to='classroom.Course'),
        ),
    ]
