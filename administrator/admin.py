from django.contrib import admin

from .models import Teknisi, Pelanggan, Slide, Tahun,Produk, DetailPasang, Perbaikan, SettingPembayaran

# Register your models here.

admin.site.register(Pelanggan)
admin.site.register(Slide)
admin.site.register(Tahun)
admin.site.register(Produk)
admin.site.register(DetailPasang)
admin.site.register(Perbaikan)
admin.site.register(SettingPembayaran)
admin.site.register(Teknisi)
