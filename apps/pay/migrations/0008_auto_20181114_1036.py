# Generated by Django 2.1.2 on 2018-11-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0007_ticketsordersmaintable_cdk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsordersmaintable',
            name='cdk',
            field=models.CharField(default='', max_length=25, verbose_name='兑换码'),
        ),
    ]
