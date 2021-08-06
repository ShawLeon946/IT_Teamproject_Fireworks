# Generated by Django 2.1.5 on 2021-08-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Middle', 'Middle'), ('Big', 'Big')], max_length=10)),
                ('type', models.CharField(choices=[('Beans', 'Beans'), ('Milk', 'Milk')], max_length=255)),
                ('sweetness', models.CharField(choices=[('100%', '100%'), ('70%', '70%'), ('30%', '30%')], max_length=10)),
            ],
        ),
    ]
