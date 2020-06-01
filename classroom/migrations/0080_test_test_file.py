# Generated by Django 3.0.5 on 2020-05-25 05:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0079_test_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_file',
            field=models.FileField(default=False, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='テスト'),
        ),
    ]
