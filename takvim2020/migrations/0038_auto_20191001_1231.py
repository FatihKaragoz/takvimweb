# Generated by Django 2.2.5 on 2019-10-01 12:31

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0037_auto_20190926_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis',
            name='pieces',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e729d521-3a4f-4b67-988a-def9206aac7b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e66ddcfc-40fd-4369-b8f1-1dfa9bb9fa75'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b0632086-9220-4c20-8ef0-6f870feaf10c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('38f79b57-c6a0-4ff0-be1a-f35eb58eb6ea'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('eeafe0c5-5c47-4448-acf8-de9218310f6a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6d0d3602-1bc6-4b5b-ae71-681b1243a635'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('ca5f2553-e1a9-4bec-aeea-4a350186581c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('406bfcad-ef8d-4aa1-b25d-49e699422acf'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b2f2d05c-41e7-496f-859b-9d373ec49907'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('8f8bd58b-c590-4c5d-a384-b8394d551fbc'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('eff070d0-7759-4a1a-9644-fa3c9ae6145d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a9ba4009-a7ac-4454-941c-a1eef57b3699'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('4caf1d0e-7c61-43d8-866e-45fce4d97cba'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
