# Generated by Django 3.0.5 on 2020-05-25 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0083_auto_20200525_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetail',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='添付ファイル'),
        ),
    ]