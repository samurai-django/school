# Generated by Django 3.0.5 on 2020-05-23 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0063_auto_20200523_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship2',
            name='students',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
