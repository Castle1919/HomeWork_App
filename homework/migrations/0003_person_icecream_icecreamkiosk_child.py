# Generated by Django 5.1.7 on 2025-04-22 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_article_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('flavor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IceCreamKiosk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('ice_creams', models.ManyToManyField(related_name='kiosks', to='homework.icecream')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homework.person')),
                ('favorite_ice_cream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homework.icecream')),
            ],
            bases=('homework.person',),
        ),
    ]
