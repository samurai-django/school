# Generated by Django 3.0.5 on 2020-05-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0058_auto_20200522_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
