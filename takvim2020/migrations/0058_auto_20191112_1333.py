# Generated by Django 2.2.5 on 2019-11-12 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0057_auto_20191105_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('3614ed80-042c-4a0c-9ea3-73b089b83f67'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('8c39a6f7-454d-4eac-b5ef-06f6449fb771'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('f92adf86-7520-411b-969d-12bfba102e00'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('8d4d7cf4-e5f7-4c6b-aabd-3909b30604c4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('7c07cdf6-72a5-40c5-b5a1-0d0e9f45edc6'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('069481eb-5b90-44cd-9457-1168427b0e26'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('74823cc7-f778-42eb-baaf-58e533b153b3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici2',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici2',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('7f934ac6-506b-4626-a1f5-76a320df5a7f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6d5f4e3f-ae40-483b-936b-505829695a0b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemicieko',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemicieko',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('fa902b86-8973-4f1b-a505-c5b1984f7327'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='instagramgonderi',
            name='gonderi_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('79abfb81-9099-4efb-82ac-f8c331e150f4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('52ba8c9c-8fb7-44cc-8b61-b8d095574f3d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('fc4759a6-da47-41b6-8692-f3ae7227434c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('923d0bca-c2f7-4b85-b01c-118576b8483a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 13, 33, 35, 675572, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('1ed8a3fb-9636-4ac3-abed-4683653c409d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('be55c02a-b245-4773-99f4-0a0ffe57dc37'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('gemicieko', 'GEMİCİ EKO'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('masaustu', 'MASAUSTU'), ('ajanda', 'AJANDA'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('ac35184d-eb46-4630-acbd-b28183bd8908'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
