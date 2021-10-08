from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from perpustakaan.viewset_api import KelompokViewset, BukuViewset
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register('kelompok', KelompokViewset)
router2 = routers.DefaultRouter()
router2.register('buku', BukuViewset)

urlpatterns = [
    url(r'^$', index, name="index"),
    path('api_kelompok/', include(router1.urls)),
    path('api_buku/', include(router2.urls)),
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('tambah-kelompok/', tambah_kelompok, name='tambah_kelompok'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('export/xls/', export_xls, name='export_xls'),
]
