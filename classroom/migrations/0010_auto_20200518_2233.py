# Generated by Django 3.0.5 on 2020-05-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0009_auto_20200518_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='student',
        ),
        migrations.AlterField(
            model_name='register',
            name='options',
            field=models.ManyToManyField(to='classroom.Class'),
        ),
        migrations.DeleteModel(
            name='ClassDetail',
        ),
    ]
