# Generated by Django 2.1.5 on 2019-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190324_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finder',
            name='image5',
            field=models.ImageField(blank='True', upload_to=''),
        ),
    ]
