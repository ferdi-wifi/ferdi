from django import forms
from django.forms import ModelForm
from .models import Teknisi, Pelanggan, Slide, Perbaikan, DetailPasang, SettingPembayaran, Produk,Tahun
from django.contrib.auth.models import User

class TahunForm(ModelForm):
    class Meta:
        model = Tahun
        fields=['nama','aktif']
    labels = {
            'nama': 'Nama Tahun:',
        } 
class ProdukForm(ModelForm):
    class Meta:
        model = Produk
        fields=['nama_produk','gambar','harga','harga_pemasangan','keterangan']
    labels = {
            'nama_produk': 'Nama Produk:',
        } 
class SlideForm(ModelForm):
    class Meta:
        model = Slide
        fields=['judul','judul_samping','gambar_slide','aktif']
class TeknisiForm(ModelForm):
    class Meta:
        model = Teknisi
        fields=['nama','wa','alamat','email']
        widgets = {
            'wa': forms.TextInput(attrs={'class': 'form-control','placeholder':'628xxxxxxxxxx'}),

        }
class PelangganForm(ModelForm):
    class Meta:
        model = Pelanggan
        fields=['nama','wa','alamat','email']
        widgets = {
            'wa': forms.TextInput(attrs={'class': 'form-control','placeholder':'628xxxxxxxxxx'}),

        }
class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['username']
        help_texts ={
            'username':''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':'required'}),
        }
        labels = {
            'username': 'Username*',
        }

class PerbaikanForm(ModelForm):
    class Meta:
        model = Perbaikan
        fields=['status','keterangan']
        labels = {
                'status': 'Ubah Status:',
            }    
class DetailPasangForm(ModelForm):
    class Meta:
        model = DetailPasang
        fields=['status','tanggal_pasang','alasan_pembatalan']
        widgets = {
                'tanggal_pasang': forms.TextInput(attrs={'type':'date','class': 'form-control'}),
            }
        labels = {
                'status': 'Ubah Status:',
                'alasan_pembatalan': 'Alasan Pembatalan *) Isi jika ada pembatalan Pemasangan:',
            }    

class AjukanPerbaikanForm(ModelForm):
    class Meta:
        model = Perbaikan
        fields=['status']
        widgets = {
                'status': forms.Select(attrs={'type':'date','class': 'form-control','required':'required'}),
            }
        labels = {
                'status': 'Ubah Status:',
            } 