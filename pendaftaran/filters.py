from .models import Pendaftar
import django_filters


class PendaftarFilter(django_filters.FilterSet):
    nama = django_filters.CharFilter(lookup_expr='icontains')
    asal_sekolah = django_filters.CharFilter(lookup_expr='icontains')
    nomor_pendaftaran = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Pendaftar
        fields = ['nomor_pendaftaran', 'nama', 'asal_sekolah', ]
