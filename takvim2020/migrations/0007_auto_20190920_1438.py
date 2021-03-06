# Generated by Django 2.2.5 on 2019-09-20 14:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('takvim2020', '0006_auto_20190920_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gemici3',
            old_name='s1price',
            new_name='price1',
        ),
        migrations.RenameField(
            model_name='gemici3',
            old_name='s2price',
            new_name='price2',
        ),
        migrations.RenameField(
            model_name='gemici3',
            old_name='s3price',
            new_name='price3',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s1color',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s1color2',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s1size',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s2color',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s2color2',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s2size',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s3color',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s3color2',
        ),
        migrations.RemoveField(
            model_name='gemici3',
            name='s3size',
        ),
        migrations.AddField(
            model_name='gemici3',
            name='size1',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Olcu1Olcu', to='takvim2020.size', verbose_name='Ölçü 1 için  boyut - renk - fotoğraglar '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gemici3',
            name='size2',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Olcu2Olcu', to='takvim2020.size', verbose_name='Ölçü 2 için boyut - renk - fotoğraflar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gemici3',
            name='size3',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Olcu3Size', to='takvim2020.size', verbose_name='Ölçü 3 için boyut - renk - fotoğraflar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='color1',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='renk1renk', to='takvim2020.color', verbose_name='Renk 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='color2',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='renk2renk', to='takvim2020.color', verbose_name='Renk 2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='color',
            name='color2_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('1057686f-2161-4537-bd7b-bfbece45be6f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='exp',
            field=models.CharField(max_length=100, verbose_name='Renk açıklama'),
        ),
        migrations.AlterField(
            model_name='color',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='colorname',
            name='color_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('c35580ee-90b7-41b0-a957-c3fe97af5e74'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA')], max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='gemici3',
            name='product_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('fdee5f46-5b34-40dd-aa92-318016e0a246'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menuItem',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='menuc',
            name='menu_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e9d0732a-b713-4de5-86be-de427f2c87f7'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='model',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA')], max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('e2b6233e-e35e-4ef9-a885-fa22bce5c20a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.CharField(choices=[('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK'), ('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='size',
            name='size_id',
            field=models.UUIDField(blank=True, default=uuid.UUID('c4dbce6d-35c3-4f1f-9399-21c28cb76d89'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
