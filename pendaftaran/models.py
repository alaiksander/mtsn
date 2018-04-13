from django.db import models
from statistics import mean

# Create your models here.

AGAMA = (
    ('Islam', 'Islam'),
    ('Kristen', 'Kristen'),
    ('Katholik', 'Katholik'),
    ('Hindu', 'Hindhu'),
    ('Budha', 'Budha'),
    ('-', '-'),
)

JENIS_KELAMIN = (
    ('Laki-laki', 'L'),
    ('Perempuan', 'P'),
)


class Pendaftar(models.Model):
    # -------- PESERTA DIDIK ---------
    nomor_pendaftaran = models.IntegerField(null=True)
    password_pendaftaran = models.CharField(max_length=5, default='12345')
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN, default='laki-laki',)
    tempat_lahir = models.CharField(max_length=15, default='Kudus')
    tanggal_lahir = models.DateField(null=True)
    agama_anak = models.CharField(max_length=10, choices=AGAMA, default='islam',)
    anak_ke = models.CharField(max_length=2)
    jumlah_saudara_kandung = models.CharField(max_length=2, blank=True)
    asal_sekolah = models.CharField(max_length=50)

    # -------- ORANGTUA/WALI ---------
    nama_ayah = models.CharField(max_length=50)
    nama_ibu = models.CharField(max_length=50)
    pendidikan_ayah = models.CharField(max_length=25)
    pendidikan_ibu = models.CharField(max_length=25)
    pekerjaan_ayah = models.CharField(max_length=30)
    pekerjaan_ibu = models.CharField(max_length=30)
    agama_ayah = models.CharField(max_length=10, choices=AGAMA, default='islam',)
    agama_ibu = models.CharField(max_length=10, choices=AGAMA, default='islam',)
    alamat_orang_tua = models.CharField(max_length=200)
    no_telepon = models.CharField(max_length=12)
    nama_wali = models.CharField(max_length=50, default='-')
    pendidikan_wali = models.CharField(max_length=50, default='-')
    agama_wali = models.CharField(max_length=10, choices=AGAMA, default='-',)
    alamat_wali = models.CharField(max_length=50, default='-')

    # ------------- KELAS 4 --------
    indo_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    mtk_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    ipa_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    indo_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0)
    mtk_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0)
    ipa_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0)

    # ------------- KELAS 5 ---------
    indo_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    mtk_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    ipa_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    indo_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0)
    mtk_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0)
    ipa_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0)

    # ------------- KELAS 6 ---------
    indo_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    mtk_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0)
    ipa_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0)

    # ------------- RATA-RATA MAPEL ---------
    # rerata_indo = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    # rerata_mtk = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    # rerata_ipa = models.DecimalField(max_digits=2, decimal_places=0, null=True)
    # rerata_mapel = models.DecimalField(max_digits=2, decimal_places=0, null=True)

    def __unicode__(self):
        return self.nama

    def get_rerata_indo(self):
        indo = [self.indo_kelas4_smt1, self.indo_kelas4_smt2, self.indo_kelas5_smt2, self.indo_kelas5_smt2, self.indo_kelas6_smt1]
        return mean(indo)

    def get_rerata_ipa(self):
        ipa = [self.ipa_kelas4_smt1, self.ipa_kelas4_smt2, self.ipa_kelas5_smt1, self.ipa_kelas5_smt2, self.ipa_kelas6_smt1]
        return self.mean(ipa)

    def get_rerata_mtk(self):
        mtk = [self.mtk_kelas4_smt1, self.mtk_kelas4_smt2, self.mtk_kelas5_smt1, self.mtk_kelas5_smt2, self.mtk_kelas6_smt1]
        return self.mean(mtk)

    # rerata_indo = get_rerata_indo()
    # rerata_ipa = get_rerata_ipa()
    # rerata_mtk = get_rerata_mtk()

    # @property
    # def get_rerata_mapel(self):
    #     rerata = [rerata_indo, rerata_ipa, rerata_mtk]
    #     return mean(rerata)

    # rerata_mapel = property(get_rerata_mapel)


# class RegistrasiUlang(models.Model):
#     nama = models.ForeignKey(Pendaftar, on_delete=models.CASCADE)
#     nisn = models.CharField(max_length=8)
#     kartu_keluarga = models.CharField(max_length=16)
#     nik = models.CharField(max_length=16)
#     hobi = models.CharField(max_length=30)
#     cita_cita = models.CharField(max_length=50)
#     prestasi = models.CharField(max_length=50)
#     nilai_skhun = models.DecimalField(max_digits=4, decimal_places=2)
#     daftar_ulang = models.BooleanField(initial='')


# class UserPassword(models.Model):
#     nama = models.ForeignKey(Pendaftar, on_delete=models.CASCADE)
#     user = models.CharField(max_length=9)
#     passw = models.CharField(max_length=5)
