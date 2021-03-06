# Generated by Django 2.2.5 on 2019-09-24 12:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0033_auto_20190924_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='color2_id',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b4b4d6db-e096-4ff5-be08-cf287ce105fd'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('cdc3c254-4c5b-46d6-8984-9ea32366d22f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('93324e77-929c-4fe2-83fa-11e71d0ea40d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2b90d2d1-5fc4-4eb2-9d79-42bbe92607b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2d46a02b-f01c-4af3-8473-6e3fe82d4d45'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a2254c91-b0e8-4eeb-b293-afe6660a63ff'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e2c35abe-d9b2-4b7d-a30e-567b227692cd'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a80687bf-e3b2-47b7-ab02-9d6d831587f0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('4a8559cc-2f3d-45d0-99e7-dcf3dcce189f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b3af6393-4a13-4f8d-a4d7-d89b6a205537'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('002a3ed4-98c9-4160-887b-c9a3f461c922'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2895c1b8-f54a-41e1-9ab4-ab68393977d5'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
