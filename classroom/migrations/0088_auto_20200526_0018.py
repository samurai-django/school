# Generated by Django 3.0.5 on 2020-05-25 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0087_auto_20200526_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourse',
            name='name',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.ClassRoomStudent'),
        ),
    ]