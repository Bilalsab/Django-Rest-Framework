# Generated by Django 2.0.7 on 2019-03-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190325_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='Address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finder',
            name='TrackAddress',
            field=models.ManyToManyField(to='api.Address'),
        ),
    ]
