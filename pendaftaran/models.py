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

SEKOLAH = (
    ('SD', 'SD'),
    ('MI', 'MI'),
)


class Pendaftar(models.Model):
    # -------- PESERTA DIDIK ---------
    nomor_pendaftaran = models.IntegerField(null=True)
    password_pendaftaran = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN, default='Laki-laki',)
    tempat_lahir = models.CharField(max_length=15, default='Kudus')
    tanggal_lahir = models.DateField(null=True)
    agama_anak = models.CharField(max_length=10, choices=AGAMA, default='Islam',)
    anak_ke = models.CharField(max_length=2)
    jumlah_saudara_kandung = models.CharField(max_length=2, blank=True)
    jenis_sekolah = models.CharField(max_length=2, choices=SEKOLAH, default='SD')
    asal_sekolah = models.CharField(max_length=50)

    # -------- ORANGTUA/WALI ---------
    nama_ayah = models.CharField(max_length=50)
    nama_ibu = models.CharField(max_length=50)
    pendidikan_ayah = models.CharField(max_length=25)
    pendidikan_ibu = models.CharField(max_length=25)
    pekerjaan_ayah = models.CharField(max_length=30)
    pekerjaan_ibu = models.CharField(max_length=30)
    agama_ayah = models.CharField(max_length=10, choices=AGAMA, default='Islam',)
    agama_ibu = models.CharField(max_length=10, choices=AGAMA, default='Islam',)
    alamat_orang_tua = models.CharField(max_length=200)
    no_telepon = models.CharField(max_length=12)
    nama_wali = models.CharField(max_length=50, default='-', blank=True)
    pendidikan_wali = models.CharField(max_length=50, default='-', blank=True)
    agama_wali = models.CharField(max_length=10, choices=AGAMA, default='-', blank=True)
    alamat_wali = models.CharField(max_length=50, default='-', blank=True)

    # ------------- KELAS 4 --------
    indo_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    mtk_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    ipa_kelas4_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    indo_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    mtk_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    ipa_kelas4_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)

    # ------------- KELAS 5 ---------
    indo_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    mtk_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    ipa_kelas5_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    indo_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    mtk_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    ipa_kelas5_smt2 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)

    # ------------- KELAS 6 ---------
    indo_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    mtk_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    ipa_kelas6_smt1 = models.DecimalField(max_digits=2, decimal_places=0, blank=False)

    def __unicode__(self):
        return self.nomor_pendaftaran

    def rerata_indo(self):
        indo = [self.indo_kelas4_smt1, self.indo_kelas4_smt2, self.indo_kelas5_smt2, self.indo_kelas5_smt2, self.indo_kelas6_smt1]
        return mean(indo)

    def rerata_ipa(self):
        ipa = [self.ipa_kelas4_smt1, self.ipa_kelas4_smt2, self.ipa_kelas5_smt1, self.ipa_kelas5_smt2, self.ipa_kelas6_smt1]
        return mean(ipa)

    def rerata_mtk(self):
        mtk = [self.mtk_kelas4_smt1, self.mtk_kelas4_smt2, self.mtk_kelas5_smt1, self.mtk_kelas5_smt2, self.mtk_kelas6_smt1]
        return mean(mtk)

    RerataIndo = property(rerata_indo)
    RerataMtk = property(rerata_ipa)
    RerataIpa = property(rerata_ipa)

    def rerata_mapel(self):
        mapel = [self.RerataIndo, self.RerataMtk, self.RerataIpa]
        return mean(mapel)

    RerataMapel = property(rerata_mapel)


class RegUlang(models.Model):
    nomor_pendaftaran = models.ForeignKey(Pendaftar, on_delete=models.CASCADE)
    nisn = models.CharField(max_length=8)
    kartu_keluarga = models.CharField(max_length=16)
    nik = models.CharField(max_length=16)
    hobi = models.CharField(max_length=100)
    cita_cita = models.CharField(max_length=100)
    prestasi = models.CharField(max_length=200)
    nilai_skhun = models.DecimalField(max_digits=4, decimal_places=2)
    daftar_ulang = models.BooleanField(default=False)
