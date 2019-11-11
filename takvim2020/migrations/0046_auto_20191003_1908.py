# Generated by Django 2.2.5 on 2019-10-03 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0045_auto_20191003_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('91a1065e-3093-4a92-82f7-e08f41d1af0f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('69e448c9-90c7-4d2a-9697-eed7eba5980d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('18e85878-e7ae-44d5-b152-f9af084cfb37'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a5a8a69e-1771-4ab5-a5e2-8766911015f0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('fb801965-fc34-431d-a1c6-7b89becd3d4c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('89b102da-a202-4a6f-91de-4c8043326046'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6170eff2-247b-4c90-9bf3-0e6f5ac84498'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('357aa3d2-58a5-4b48-8d2f-cd83ac362cab'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('804618db-1517-4de6-b56c-9a679c67f3a1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('118fe18b-a8f0-4c2c-971c-11e23b88969c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 19, 8, 21, 14415, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='design',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Üst tasarım'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('08e8addc-b754-4d30-8b8f-44d4e47b19b1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d90f70ae-51f0-4314-bb36-272938149929'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6c737516-56cb-42b1-acfb-b777878d2120'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
