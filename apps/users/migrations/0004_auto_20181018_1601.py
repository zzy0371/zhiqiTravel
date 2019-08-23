# Generated by Django 2.1.2 on 2018-10-18 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myuser_check_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='名称')),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.AreaInfo', verbose_name='父级名称')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2018, 10, 18, 16, 1, 11, 292082), verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='居住城市'),
        ),
    ]
