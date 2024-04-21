# Generated by Django 5.0.4 on 2024-04-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='comment',
            field=models.ManyToManyField(to='client.comment'),
        ),
    ]
