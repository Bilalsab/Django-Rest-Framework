# Generated by Django 2.0.7 on 2019-03-25 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_finder_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='finder',
            name='TrackImage',
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.finder'),
        ),
        migrations.AddField(
            model_name='finder',
            name='TrackImage',
            field=models.ManyToManyField(to='api.Images'),
        ),
    ]
