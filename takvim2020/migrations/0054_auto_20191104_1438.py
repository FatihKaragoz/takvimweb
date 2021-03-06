# Generated by Django 2.2.5 on 2019-11-04 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0053_auto_20191009_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('f7f78ce3-e9f3-4908-84bc-5dad87c229a8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('41a2a740-4430-4f00-8055-f8d1f7ed1800'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d7f977da-9300-425f-923b-e1beb67002f9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e8576f24-4334-4682-807f-96dfa142b0f1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('9173e3f4-1cf2-439c-8150-b2e67d576719'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6f24cab8-e472-4983-b863-468de29f4fa1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('64359c91-7c31-4021-a5a0-96c2e8450cb2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('c5f9965c-e3a7-4570-840f-a139017d5ead'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('f1498b3b-ce5d-418f-bdea-2a2ab5479ce4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a9ec14d4-9796-40c5-a3f2-e1dab6b974f6'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price1000_2000',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat (1000-5000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price100_200',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Fiyat (100-200 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price2000_5000',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat (1000-5000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price200_500',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat (200-500 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price500_1000',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat (500-1000 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price50_100',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Fiyat (50-100 adet için)'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b1f35d35-3068-4095-b02e-e8b6ae49efd1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 14, 38, 31, 678319, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d0e7ef1c-99f1-40f1-b99e-fead286e49b7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('eadae79f-3efd-4bee-bfe4-e03cb8b735de'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('82e6243f-7ee4-420b-9fd1-635822880a1e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
