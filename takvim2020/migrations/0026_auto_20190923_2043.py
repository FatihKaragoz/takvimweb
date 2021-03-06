# Generated by Django 2.2.5 on 2019-09-23 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('takvim2020', '0025_auto_20190923_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('406c4b57-afb8-40e7-879d-a6ed49fd59e9'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2e888088-7e10-4e3e-ae87-90afa85c312d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('25e5730b-c3d3-42f4-ba7c-a9e071d9f32a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('c1ea590a-06e3-409c-b317-28490dd3c345'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('ad2e391d-8603-4be2-9a62-24cda3425c75'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('624f8a80-ec32-42cc-b571-be0b2b28390a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('5eca2107-f34c-4f2a-8741-e252a848083e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('80f4cabd-aed3-445c-9208-2bafd58979b8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('4dd8cce5-118e-438d-bd7a-098f60e20a76'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='ajanda',
            fields=[
                ('product_id', models.UUIDField(blank=True, default=uuid.UUID('9ea1b93a-ce71-4e6f-b5af-91db520e445d'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('ajanda', 'AJANDA'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('masaustu', 'MASAUSTU'), ('gemici3', 'GEMİCİ 3 Spiral')], max_length=20, verbose_name='Kategori')),
                ('name', models.CharField(default='AJANDA', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Olcu1Ajanda', to='takvim2020.size', verbose_name='Ölçü 1 için  boyut - renk - fotoğraglar')),
            ],
        ),
    ]
