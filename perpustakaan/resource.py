from import_export import resources
from import_export.fields import Field
from perpustakaan.models import Buku

class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='Kelompok')
    judul = Field(attribute='judul', column_name='Judul')
    penerbit = Field(attribute='penerbit', column_name='Penerbit')
    jumlah = Field(attribute='jumlah', column_name='Jumlah')

    class Meta:
        model = Buku
        fields = ['judul', 'kelompok_id__nama', 'penerbit', 'jumlah']
        export_order = ['judul','kelompok_id__nama','penerbit','jumlah']