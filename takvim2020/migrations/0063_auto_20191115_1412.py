# Generated by Django 2.2.5 on 2019-11-15 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0062_auto_20191115_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanda',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='ajanda',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('016370b4-7b31-43e4-bb55-6987f561f7f8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('518ec659-27ff-4408-b6ef-15ce28e093d3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d2040742-af83-4b86-b1e1-bcdd1039be9f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('09a2051e-8ca5-4e47-b3b2-b6eb973a138f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a9bc8ddd-7b31-41ac-a9e5-fc856e58baab'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('2ff43f49-6dbc-4544-83ba-ff4c509508f8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici1',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e96204be-1834-450c-aa09-3fe69552491a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici2',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici2',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('9ba03e43-0dbf-4507-b073-01b780844e45'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e11ade18-8cd5-4f1d-8e83-319266018715'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemicieko',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemicieko',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('8ade0336-e038-4376-9c3b-5a48f95d4797'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='instagramgonderi',
            name='gonderi_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('9ad50a88-d9a0-49c6-bde4-e445e4fb791a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='masaustu',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('9614ce6f-c3ec-4e2d-9cc1-121b9e959b8a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='created',
            field=models.CharField(default='1573827126.2904363', max_length=50),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e12d07bb-307e-4f68-97c2-6f80fa80fdcf'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('46820bd4-70ef-44b3-a84a-b6b6e5442c67'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 14, 12, 6, 298457, tzinfo=utc), verbose_name='Siparis zamanı'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='product_id',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='siparis_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('bedbe5ac-c4cd-4413-8aaf-2a4825772cd2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('0b00c173-4ea1-4512-b11d-32c88e9ce8ec'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('gemicieko', 'GEMİCİ EKO'), ('ajanda', 'AJANDA'), ('gemici2', 'GEMİCİ 2 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('gemici1', 'GEMİCİ 1 Spiral')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created',
            field=models.CharField(default='1573827126.2978683', max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('a59abd79-d3e7-438b-8d77-ec27ebf8eb5e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
