# Generated by Django 4.1.1 on 2023-03-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_image_users_like_product_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.CharField(default='$', max_length=100),
        ),
    ]