# Generated by Django 2.2.5 on 2019-09-23 20:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0024_auto_20190923_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('43fa2726-4eee-4340-a2b7-ac3893889079'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('33deb85b-e6e8-41d8-8123-0eb32bbed322'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('b0f5ddfe-614a-4247-9c45-9fd391186fbc'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('5365d695-ba9e-4db1-a460-6fac35e5e012'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('37aa0743-8ae4-4e6a-9b18-c3567472f538'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('47977cb3-790c-48c9-9fdb-c0a72e056b94'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('0b060369-1d67-42dd-b2d3-9a282e893197'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('960f52f9-4845-4986-bd4b-835ef7b03e5e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='color2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='renk2renk', to='takvim2020.color', verbose_name='Renk 2'),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('46f04c5f-535c-4b40-a6c2-5bdbaff4ade0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
