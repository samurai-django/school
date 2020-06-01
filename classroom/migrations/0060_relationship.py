# Generated by Django 3.0.5 on 2020-05-21 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0059_auto_20200522_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_registered', models.BooleanField(default=False)),
                ('classes', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.Class')),
                ('register', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.Register')),
            ],
        ),
    ]