# Generated by Django 3.0.5 on 2020-05-18 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0016_remove_register_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='teachers',
            field=models.ManyToManyField(related_name='register_teachers', to=settings.AUTH_USER_MODEL),
        ),
    ]
