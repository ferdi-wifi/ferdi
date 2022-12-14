# Generated by Django 3.1.7 on 2022-07-01 22:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('gambar', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, size=[700, 400], upload_to='gambar/produk', verbose_name='Gambar (700 x 400 pixel)*)')),
                ('harga', models.PositiveIntegerField(null=True)),
                ('harga_pemasangan', models.PositiveIntegerField(null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('keterangan', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Produk',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=200, null=True)),
                ('judul_samping', models.CharField(blank=True, max_length=200, null=True)),
                ('kalimat', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar_slide', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, size=[1400, 600], upload_to='gambar/slide', verbose_name='Gambar Slide (1400 x 600 pixel) *)')),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Slide',
            },
        ),
        migrations.CreateModel(
            name='Tahun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.CharField(max_length=200, null=True)),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tahun',
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('wa', models.CharField(max_length=200, null=True, verbose_name='No Whatsapp')),
                ('alamat', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Custumer',
            },
        ),
    ]
