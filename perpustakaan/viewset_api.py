from perpustakaan.models import Kelompok, Buku
from perpustakaan.serializers import KelompokSerializer, BukuSerializer
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializer
    permission_classes = [permissions.IsAuthenticated]

class BukuViewset(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    permission_classes = [permissions.IsAuthenticated]