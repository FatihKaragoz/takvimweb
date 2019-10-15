# Generated by Django 2.2.5 on 2019-09-23 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('takvim2020', '0023_auto_20190921_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('cef8c0b3-6cc9-4a08-98ae-1c98e20b430d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4756ecb-2edd-4a72-ba31-8abea2f8650a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('74548570-5311-4e77-8d96-912c82603d09'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('200456d3-3313-45e4-964e-bf5f30ff7c45'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('7e02679e-5939-4c24-a148-e1b13465a230'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2b41841a-c6cc-4e05-9297-f6312e2c10e1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='masaustu',
            fields=[
                ('product_id', models.UUIDField(blank=True, default=uuid.UUID('7133314b-b0d7-4ea2-ab69-e8d412d54fee'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=20, verbose_name='Kategori')),
                ('name', models.CharField(default='MASAÜSTÜ', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Olcu1Masaustu', to='takvim2020.size', verbose_name='Ölçü 1 için  boyut - renk - fotoğraglar')),
                ('size2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Olcu2Masaustu', to='takvim2020.size', verbose_name='Ölçü 2 için boyut - renk - fotoğraflar')),
            ],
        ),
        migrations.CreateModel(
            name='gemici1',
            fields=[
                ('product_id', models.UUIDField(blank=True, default=uuid.UUID('5cae1515-7fad-43ca-8776-66c699e0755a'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='GEMİCİ 3 Spiral', max_length=50)),
                ('category', models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=20, verbose_name='Kategori')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OlcuGemici', to='takvim2020.size', verbose_name='Ölçü 1 için  boyut - renk - fotoğraglar ')),
            ],
        ),
        migrations.CreateModel(
            name='akademik',
            fields=[
                ('product_id', models.UUIDField(blank=True, default=uuid.UUID('671b5dfe-5292-428d-992b-298ed87d4c23'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('gemici3', 'GEMİCİ 3 Spiral'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU')], max_length=20, verbose_name='Kategori')),
                ('name', models.CharField(default='AKADEMİK', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OlcuAkademik', to='takvim2020.size', verbose_name='Boyut - Renk - Fotoğraf')),
            ],
        ),
    ]
