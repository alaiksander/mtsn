# Generated by Django 2.0.2 on 2018-04-07 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pendaftar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_pendaftaran', models.CharField(max_length=10)),
                ('password_pendaftaran', models.CharField(default='12345', max_length=5)),
                ('nama', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('laki-laki', 'L'), ('perempuan', 'P')], default='laki-laki', max_length=10)),
                ('tempat_lahir', models.CharField(default='Kudus', max_length=15)),
                ('tanggal_lahir', models.DateField(help_text='Format: tahun-bulan-hari, misal: 2000-04-12', null=True)),
                ('agama_anak', models.CharField(choices=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katholik', 'Katholik'), ('hindu', 'Hindhu'), ('budha', 'Budha'), ('-', '-')], default='islam', max_length=10)),
                ('anak_ke', models.CharField(max_length=2)),
                ('jumlah_saudara_kandung', models.CharField(blank=True, max_length=2)),
                ('asal_sekolah', models.CharField(max_length=50)),
                ('nama_ayah', models.CharField(max_length=50)),
                ('nama_ibu', models.CharField(max_length=50)),
                ('pendidikan_ayah', models.CharField(max_length=25)),
                ('pendidikan_ibu', models.CharField(max_length=25)),
                ('pekerjaan_ayah', models.CharField(max_length=30)),
                ('pekerjaan_ibu', models.CharField(max_length=30)),
                ('agama_ayah', models.CharField(choices=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katholik', 'Katholik'), ('hindu', 'Hindhu'), ('budha', 'Budha'), ('-', '-')], default='islam', max_length=10)),
                ('agama_ibu', models.CharField(choices=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katholik', 'Katholik'), ('hindu', 'Hindhu'), ('budha', 'Budha'), ('-', '-')], default='islam', max_length=10)),
                ('alamat_orang_tua', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=12)),
                ('nama_wali', models.CharField(default='-', max_length=50)),
                ('pendidikan_wali', models.CharField(default='-', max_length=50)),
                ('agama_wali', models.CharField(choices=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katholik', 'Katholik'), ('hindu', 'Hindhu'), ('budha', 'Budha'), ('-', '-')], default='-', max_length=10)),
                ('alamat_wali', models.CharField(default='-', max_length=50)),
                ('indo_kelas4_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mtk_kelas4_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ipa_kelas4_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('indo_kelas4_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mtk_kelas4_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ipa_kelas4_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('indo_kelas5_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mtk_kelas5_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ipa_kelas5_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('indo_kelas5_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mtk_kelas5_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ipa_kelas5_smt2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('indo_kelas6_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('mtk_kelas6_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('ipa_kelas6_smt1', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrasiUlang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nisn', models.CharField(max_length=8)),
                ('kartu_keluarga', models.CharField(max_length=16)),
                ('nik', models.CharField(max_length=16)),
                ('hobi', models.CharField(max_length=30)),
                ('cita_cita', models.CharField(max_length=50)),
                ('prestasi', models.CharField(max_length=50)),
                ('nilai_skhun', models.DecimalField(decimal_places=2, max_digits=4)),
                ('nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran.Pendaftar')),
            ],
        ),
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=9)),
            ],
        ),
    ]
