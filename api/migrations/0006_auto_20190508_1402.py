# Generated by Django 2.2 on 2019-05-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekorder',
            old_name='month',
            new_name='mark',
        ),
    ]