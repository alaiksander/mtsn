from django.contrib import admin
from .models import Pendaftar
# from .models import Pendaftar, RegistrasiUlang
# Register your models here.


class PendaftarList(admin.ModelAdmin):
    list_display = ('nomor_pendaftaran', 'nama', 'asal_sekolah')


admin.site.register(Pendaftar, PendaftarList)
