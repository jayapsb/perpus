from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku, Kelompok

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = ['judul','penulis','penerbit','kelompok_id','jumlah'] # tampilkan field tertentu saja
        widgets = {
            'judul': forms.TextInput({'class':'form-control', 'placeholder':"Judul"}),
            'penulis': forms.TextInput({'class':'form-control', 'placeholder':"Penulis"}),
            'penerbit': forms.TextInput({'class':'form-control', 'placeholder':"Penerbit"}),
            'kelompok_id': forms.Select({'class':'form-control', 'placeholder':"Kelompok"}),
            'jumlah': forms.NumberInput({'class':'form-control', 'placeholder':"Jumlah"}),
        }

class FormKelompok(ModelForm):
    class Meta:
        model = Kelompok
        fields = '__all__' # tampilkan semua field 
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.Textarea({'class':'form-control'}),
        }