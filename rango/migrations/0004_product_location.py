# Generated by Django 2.1.5 on 2021-08-06 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
