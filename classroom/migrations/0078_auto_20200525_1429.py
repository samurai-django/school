# Generated by Django 3.0.5 on 2020-05-25 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0077_remove_coursedetail_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.CourseDetail')),
            ],
        ),
        migrations.AlterField(
            model_name='score',
            name='course',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='classroom.Test'),
        ),
    ]