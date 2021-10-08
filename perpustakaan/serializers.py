from perpustakaan.models import Kelompok, Buku
from rest_framework import serializers

class KelompokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields = ['id', 'nama', 'keterangan']

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id', 'judul', 'penulis', 'penerbit', 'jumlah', 'kelompok_id']