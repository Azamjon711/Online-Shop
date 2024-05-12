# Generated by Django 5.0.4 on 2024-05-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_remove_customer_comment_delete_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['id'], name='client_cust_id_647113_idx'),
        ),
    ]