from django.shortcuts import render, get_object_or_404, redirect
from administrator.models import Pelanggan,Slide, Perbaikan, DetailPasang, SettingPembayaran, Produk,Tahun
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from datetime import datetime, timedelta, time
today = datetime.now().date()
from administrator.forms import PerbaikanForm
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna,pilihan_login
from django.http import JsonResponse

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['teknisi']) 
def beranda_teknisi (request):

    jmlproduk = Produk.objects.all().count()
    jmlpelanggan = Pelanggan.objects.all().count()
    jmlperbaikan = Perbaikan.objects.all().count()
    jmlslide = Slide.objects.all().count()
    jmltahun = Tahun.objects.all().count()
    jmlbelumbayar = SettingPembayaran.objects.filter(date_created=today).count()
    context = {
        'judul': 'Halaman Beranda Teknisi',
        'menu': 'beranda',
        'jmlproduk':jmlproduk,
        'jmlpelanggan':jmlpelanggan,
        'jmlslide':jmlslide,
        'jmltahun':jmltahun,
        'jmlbelumbayar':jmlbelumbayar,
        'jmlperbaikan':jmlperbaikan


    }
    return render(request, 'teknisi_beranda.html', context)

