# Generated by Django 2.2.5 on 2019-10-03 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0043_auto_20191003_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2003e4a3-ee16-4906-ba6c-d7bd77ebeea3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6e5aca90-3a8c-478a-b6c9-88d434402c75'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d5891b71-1a8f-46eb-bd86-dcba22b9e92e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('9283240b-c56a-4100-bf82-c3cfddaf9c9e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('7e49bbff-f498-4fd4-a5ca-de96e3aa0fc1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2015de2f-26d6-4aee-b8ae-d508736eaa57'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('3b589b3d-37b1-408f-999e-977fac656122'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6143c496-a8cb-42fb-92c6-2a1e2c560634'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('c19e26ad-3b52-4389-ad3a-d94590ac24c3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price1000_2000',
            field=models.FloatField(verbose_name='Fiyat (1000-5000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price100_200',
            field=models.FloatField(verbose_name='Fiyat (100-200 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price2000_5000',
            field=models.FloatField(verbose_name='Fiyat (1000-5000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price200_500',
            field=models.FloatField(verbose_name='Fiyat (200-500 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price500_1000',
            field=models.FloatField(verbose_name='Fiyat (500-1000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price50_100',
            field=models.FloatField(verbose_name='Fiyat (50-100 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('df4e99a9-4fd4-4b87-8ca2-76666cf99146'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 14, 11, 57, 805766, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('ce39d9c5-1ad5-46fd-afeb-0d141605f0c1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a7398ff5-2521-4456-9c8c-2dc857e6d2a8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('043a0562-c7ca-4975-a21b-507c3d94c24c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
