# Generated by Django 3.0.5 on 2020-05-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0018_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='tags',
            field=models.ManyToManyField(to='classroom.Tag'),
        ),
    ]