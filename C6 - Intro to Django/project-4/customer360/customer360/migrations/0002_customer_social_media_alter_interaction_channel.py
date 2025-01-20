# Generated by Django 5.1.5 on 2025-01-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='social_media',
            field=models.CharField(default='twitter', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interaction',
            name='channel',
            field=models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter'), ('social_media', 'Social Media')], max_length=15),
        ),
    ]
