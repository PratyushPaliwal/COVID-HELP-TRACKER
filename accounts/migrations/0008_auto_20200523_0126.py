# Generated by Django 2.2.7 on 2020-05-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200520_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lattitude',
            field=models.DecimalField(decimal_places=3, default=25.531, max_digits=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='longitude',
            field=models.DecimalField(decimal_places=3, default=73.909, max_digits=8),
        ),
    ]
