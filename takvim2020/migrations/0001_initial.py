# Generated by Django 2.2.5 on 2019-09-19 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menuC',
            fields=[
                ('menu_id', models.UUIDField(blank=True, default=uuid.UUID('ffa9e35f-864a-48e2-b5ef-b6f1847960ae'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('menuItem', models.CharField(choices=[('gemici1', 'GEMİCİ 1 Spiral'), ('gemici3', 'GEMİCİ 3 Spiral'), ('ajanda', 'AJANDA'), ('masaustu', 'MASAUSTU'), ('akademik', 'AKADEMİK')], max_length=50, verbose_name='category')),
                ('menuposition', models.IntegerField(choices=[(1, 'Büyük'), (2, 'Küçük')], verbose_name='menudeki pozisyon')),
                ('image', models.ImageField(upload_to='', verbose_name='Menü Resmi')),
            ],
        ),
    ]
