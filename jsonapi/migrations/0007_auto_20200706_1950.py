# Generated by Django 3.0.8 on 2020-07-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0006_auto_20200706_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='tz',
            field=models.CharField(max_length=200),
        ),
    ]
