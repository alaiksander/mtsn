from django.shortcuts import render, get_object_or_404, redirect
from .models import Pendaftar
from .forms import PendaftarForm
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from statistics import mean
from django.http import HttpResponse
import csv
from .filters import PendaftarFilter
import random


# Create your views here.

def landing(request):
    return render(request, 'ppdb/landing.html',)


def ppdb(request):
    jumlah = Pendaftar.objects.all().count()
    dariSD = Pendaftar.objects.filter(jenis_sekolah='SD').count()
    dariMI = Pendaftar.objects.filter(jenis_sekolah='MI').count()
    return render(request, 'ppdb/dashboard.html', {'jumlah': jumlah, 'dariSD': dariSD, 'dariMI': dariMI})


''' Detail Pendaftar '''


def pendaftar_detail(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)
    return render(request, 'ppdb/pendaftar_detail.html', {'pendaftar': pendaftar})


''' Pendaftar  List'''


def pendaftar_list(request):
    pendaftar = Pendaftar.objects.all()
    pendaftar = Pendaftar.objects.order_by('-pk')
    filter = PendaftarFilter(request.GET, queryset=pendaftar)
    return render(request, 'ppdb/pendaftar.html', {'filter': filter, 'pendaftar': pendaftar, })


''' Tambah Pendaftar '''


def pendaftar_new(request):
    if request.method == "POST":
        form = PendaftarForm(request.POST)
        if form.is_valid():
            pendaftar = form.save(commit=False)
            pendaftar.save()
            pendaftar.nomor_pendaftaran = pendaftar.id + 2018000
            pendaftar.password_pendaftaran = random.randint(10000, 90000)
            pendaftar.save(update_fields=['nomor_pendaftaran', 'password_pendaftaran'])
            return redirect('pendaftar_list')

    else:
        form = PendaftarForm()
    return render(request, 'ppdb/form_daftar.html', {'form': form})


''' Edit Pendaftar '''


def pendaftar_edit(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)
    if request.method == "POST":
        form = PendaftarForm(request.POST, instance=pendaftar)
        if form.is_valid():
            pendaftar = form.save(commit=False)
            pendaftar.save()
            return redirect('pendaftar_detail', pk=pendaftar.pk)
    else:
        form = PendaftarForm(instance=pendaftar)
    return render(request, 'ppdb/form_edit.html', {'form': form})


''' Hapus Pendaftar '''


def pendaftar_delete(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)
    if request.method == 'POST':
        form = PendaftarForm(request.POST, instance=pendaftar)
        pendaftar.delete()
        pendaftar.refresh_from_db()
        return redirect('pendaftar_list')
    else:
        form = PendaftarForm(instance=pendaftar)
    return render(request, 'ppdb/pendaftar_hapus.html', {'pendaftar': pendaftar})


'''Export database ke csv'''


def export_pendaftar(request):
    export_db = HttpResponse(content_type='text/csv')
    export_db['Content-Disposition'] = 'attachment; filename="ppdb_emis.csv"'

    writer = csv.writer(export_db)
    writer.writerow(['id', 'nama', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'agama_anak',
                     'anak_ke', 'jumlah_saudara_kandung', 'asal_sekolah', 'nama_ayah', 'nama_ibu', 'pendidikan_ayah',
                     'pendidikan_ibu', 'pekerjaan_ayah', 'pekerjaan_ibu', 'agama_ayah', 'agama_ibu', 'alamat_orang_tua',
                     'no_telepon', 'nama_wali', 'pendidikan_wali', 'agama_wali', 'alamat_wali'])

    pendaftars = Pendaftar.objects.all().values_list('id', 'nama', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir',
                                                     'agama_anak', 'anak_ke', 'jumlah_saudara_kandung', 'asal_sekolah', 'nama_ayah', 'nama_ibu',
                                                     'pendidikan_ayah', 'pendidikan_ibu', 'pekerjaan_ayah', 'pekerjaan_ibu', 'agama_ayah', 'agama_ibu', 'alamat_orang_tua',
                                                     'no_telepon', 'nama_wali', 'pendidikan_wali', 'agama_wali', 'alamat_wali',)
    for pendaftar in pendaftars:
        writer.writerow(pendaftar)

    return export_db


def export_pendaftar_nilai(request):
    export_db = HttpResponse(content_type='text/csv')
    export_db['Content-Disposition'] = 'attachment; filename="ppdb_nilai.csv"'

    writer = csv.writer(export_db)
    writer.writerow(['id', 'nomor_pendaftaran', 'nama', 'indo_kelas4_smt1', 'mtk_kelas4_smt1', 'ipa_kelas4_smt1', 'indo_kelas4_smt2',
                     'mtk_kelas4_smt2', 'ipa_kelas4_smt2', 'indo_kelas5_smt1', 'mtk_kelas5_smt1', 'ipa_kelas5_smt1', 'indo_kelas5_smt2', 'mtk_kelas5_smt2',
                     'ipa_kelas5_smt2', 'indo_kelas6_smt1', 'mtk_kelas6_smt1', 'ipa_kelas6_smt1'])

    pendaftars = Pendaftar.objects.all().values_list('id', 'nomor_pendaftaran', 'nama', 'indo_kelas4_smt1', 'mtk_kelas4_smt1', 'ipa_kelas4_smt1', 'indo_kelas4_smt2',
                                                     'mtk_kelas4_smt2', 'ipa_kelas4_smt2', 'indo_kelas5_smt1', 'mtk_kelas5_smt1', 'ipa_kelas5_smt1', 'indo_kelas5_smt2', 'mtk_kelas5_smt2',
                                                     'ipa_kelas5_smt2', 'indo_kelas6_smt1', 'mtk_kelas6_smt1', 'ipa_kelas6_smt1')
    for pendaftar in pendaftars:
        writer.writerow(pendaftar)

    return export_db


def export_cbt(request):
    export_db = HttpResponse(content_type='text/csv')
    export_db['Content-Disposition'] = 'attachment; filename="ppdb_cbt.csv"'

    writer = csv.writer(export_db)
    writer.writerow(['id', 'nama', 'nomor_pendaftaran', 'password_pendaftaran'])

    pendaftars = Pendaftar.objects.all().values_list('id', 'nama', 'nomor_pendaftaran', 'password_pendaftaran')
    for pendaftar in pendaftars:
        writer.writerow(pendaftar)

    return export_db


def export_page(request):
    return render(request, 'ppdb/export.html')


def registered(request):
    return render(request, 'ppdb/registered.html')


def print_pendaftar(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)
    return render(request, 'ppdb/cetak_pendaftar.html', {'pendaftar': pendaftar})


def daftar_ulang(request):
    return render(request, 'ppdb/daftar_ulang.html')
