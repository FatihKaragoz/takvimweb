# Generated by Django 2.2.5 on 2019-10-05 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0048_auto_20191004_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuc',
            name='menuExp',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Menüde görülecek isim'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('78101c5e-9590-4d2a-a97a-2edcfac128b0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b93b7b68-0b69-4e13-af4f-04264f993aec'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('0f74fb12-cfda-460e-a1dd-baf836dfab9f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('1bd585c7-413d-4c3b-bd32-1c79d897fdc3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('cb27407d-84df-4f84-b833-3adae1ffcf9a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('8a6cb9d1-f244-4c28-bb73-00452be0358e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('0ca5f691-668e-4e44-8967-b9da642e4bee'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('22fcfa6a-b267-4ffb-a08e-a63757055e51'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('fd358da7-6c1d-4431-99a9-c5199c9cd0e3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('0a4ca4eb-39b6-4ac2-91d2-02085d18f05f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 5, 8, 53, 39, 911147, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('27b472b3-80b1-4802-9565-10a18bd7522d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('42553258-223c-4d42-81f1-4cc7f41af785'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('3d7eff2d-2210-4a86-93cc-16a101082613'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
