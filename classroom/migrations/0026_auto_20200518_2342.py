# Generated by Django 3.0.5 on 2020-05-18 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0025_auto_20200518_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='register',
            name='teachers',
        ),
        migrations.AddField(
            model_name='register',
            name='classes',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.Class'),
        ),
    ]
