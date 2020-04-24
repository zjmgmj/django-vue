# Generated by Django 2.2 on 2019-05-07 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190507_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('createTime', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
