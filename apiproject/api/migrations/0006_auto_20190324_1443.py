# Generated by Django 2.1.5 on 2019-03-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_finder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'IN_Active')], max_length=25),
        ),
    ]