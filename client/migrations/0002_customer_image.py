# Generated by Django 5.0.4 on 2024-04-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default=1, upload_to='media/client/customer/'),
            preserve_default=False,
        ),
    ]
