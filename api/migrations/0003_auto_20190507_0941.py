# Generated by Django 2.2 on 2019-05-07 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190507_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderWeight',
            new_name='weight',
        ),
    ]
