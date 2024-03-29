# Generated by Django 2.1.2 on 2019-08-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenicspots', '0004_auto_20181119_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='spots',
            name='x',
            field=models.DecimalField(decimal_places=6, default=112.460033, max_digits=9, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='spots',
            name='y',
            field=models.DecimalField(decimal_places=6, default=34.624376, max_digits=9, verbose_name='纬度'),
        ),
    ]
