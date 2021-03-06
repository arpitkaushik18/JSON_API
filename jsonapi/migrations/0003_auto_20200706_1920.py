# Generated by Django 3.0.8 on 2020-07-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0002_auto_20200706_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='real_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='tz',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='jsonapi.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
