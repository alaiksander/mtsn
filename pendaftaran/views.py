from django.shortcuts import render, get_object_or_404, redirect
from .models import Pendaftar, RegUlang
from .forms import PendaftarForm, RegUlangForm
from django.template.loader import render_to_string
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from statistics import mean
from django.http import HttpResponse
import csv
from .filters import PendaftarFilter
import random
from django.db.models import Q

# Create your views here.


def landing(request):
    template = 'ppdb/landing.html'
    return render(request, template)


def ppdb(request):
    jumlah = Pendaftar.objects.all().count()
    dariSD = Pendaftar.objects.filter(jenis_sekolah='SD').count()
    dariMI = Pendaftar.objects.filter(jenis_sekolah='MI').count()

    template = 'ppdb/dashboard.html'
    context = {
        'jumlah': jumlah,
        'dariSD': dariSD,
        'dariMI': dariMI,
    }
    return render(request, template, context)


### PENDAFTARAN ###
''' Detail Pendaftar '''


def pendaftar_detail(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)

    template = 'ppdb/pendaftar_detail.html'
    context = {
        'pendaftar': pendaftar,
    }
    return render(request, template, context)


''' Pendaftar  List'''


def pendaftar_list(request):
    pendaftar = Pendaftar.objects.all()
    pendaftar = Pendaftar.objects.order_by('-pk')
    filter = PendaftarFilter(request.GET, queryset=pendaftar)

    template = 'ppdb/pendaftar.html'
    context = {
        'filter': filter,
        'pendaftar': pendaftar,
    }
    return render(request, template, context)


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
            pendaftar_no = pendaftar.nomor_pendaftaran
            pendaftar_nama = pendaftar.nama
            pendaftar_tempat_lahir = pendaftar.tempat_lahir
            pendaftar_tanggal_lahir = pendaftar.tanggal_lahir
            pendaftar_asal_sekolah = pendaftar.asal_sekolah

            return render(request, 'ppdb/registered.html', {
                'pendaftar_no': pendaftar_no,
                'pendaftar_nama': pendaftar_nama,
                'pendaftar_tempat_lahir': pendaftar_tempat_lahir,
                'pendaftar_tanggal_lahir': pendaftar_tanggal_lahir,
                'pendaftar_asal_sekolah': pendaftar_asal_sekolah
            })

    else:
        form = PendaftarForm()
    return render(request, 'ppdb/pendaftar_form.html', {'form': form, })


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
        return redirect('pendaftar_list')
    else:
        form = PendaftarForm(instance=pendaftar)
    return render(request, 'ppdb/pendaftar_hapus.html', {'pendaftar': pendaftar})


def print_pendaftar(request, pk):
    pendaftar = get_object_or_404(Pendaftar, pk=pk)
    return render(request, 'ppdb/pendaftar_cetak.html', {'pendaftar': pendaftar})

######## REGISTRASI ULANG #########


def daftar_ulang(request):
    return render(request, 'ppdb/daftar_ulang.html')


def input_regulang(request):
    pendaftar = get_object_or_404(Pendaftar, pk=nomor_pendaftaran)
    query = pendaftar.objects.get(nomor_pendaftaran)
    if query:
        return redirect('formulir_ulang')
    else:
        return render(request, 'ppdb/input_regulang.html')
    return render(request, 'ppdb/form_daftar_ulang.html')


def formulir_ulang(request, pk):
    regulang = get_object_or_404(Pendaftar, pk=q)
    if request.method == "POST":
        form = RegUlangForm(request.POST)
        if form.is_valid():
            regulang = form.save(commit=false)
            regulang.save()
            return render(request, 'ppdb/reg_sukses.html', {'form': form})
    else:
        form = RegUlangForm()
    return render(request, 'ppdb/form_daftar_ulang.html',)

    # nomor = get_object_or_404(RegUlang, pk=pk)
    # if request.method == "GET":
    #     form = RegUlangForm(request.POST)
    #     if form.is_valid():



######## EXPORT #############
'''Export database ke csv'''


def export_page(request):
    return render(request, 'ppdb/pendaftar_export.html')


def export_pendaftar(request):
    export_db = HttpResponse(content_type='text/csv')
    export_db['Content-Disposition'] = 'attachment; filename="ppdb_emis.csv"'

    writer = csv.writer(export_db)
    writer.writerow(['No', 'Nama', 'Jenis Kelamin', 'Tempat Lahir', 'Tanggal Lahir', 'Agama',
                     'Anak ke-', 'Jumlah Saudara', 'Asal Sekolah', 'Nama Ayah', 'Nama Ibu', 'Pendidikan Ayah',
                     'Pendidikan Ibu', 'Pekerjaan Ayah', 'Pekerjaan Ibu', 'Agama Ayah', 'Agama Ibu', 'Alamat Orang Tua',
                     'No Telepon', 'Nama Wali', 'Pendidikan Wali', 'Agama Wali', 'Alamat Wali'])

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
