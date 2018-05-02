from django import forms
from .models import Pendaftar, RegUlang


class PendaftarForm(forms.ModelForm):
    class Meta:
        model = Pendaftar
        fields = '__all__'
        exclude = {'nomor_pendaftaran', 'password_pendaftaran', }
        labels = {
            'nama': ('Nama lengkap'),
            'agama_anak': ('Agama'),
            'jumlah_saudara_kandung': ('Saudara kandung'),
            # Kelas 4
            'indo_kelas4_smt1': ('Bahasa Indonesia'),
            'mtk_kelas4_smt1': ('Matematika'),
            'ipa_kelas4_smt1': ('IPA'),
            'indo_kelas4_smt2': ('Bahasa Indonesia'),
            'mtk_kelas4_smt2': ('Matematika'),
            'ipa_kelas4_smt2': ('IPA'),

            # Kelas 5
            'indo_kelas5_smt1': ('Bahasa Indonesia'),
            'mtk_kelas5_smt1': ('Matematika'),
            'ipa_kelas5_smt1': ('IPA'),
            'indo_kelas5_smt2': ('Bahasa Indonesia'),
            'mtk_kelas5_smt2': ('Matematika'),
            'ipa_kelas5_smt2': ('IPA'),

            # Kelas 6
            'indo_kelas6_smt1': ('Bahasa Indonesia'),
            'mtk_kelas6_smt1': ('Matematika'),
            'ipa_kelas6_smt1': ('IPA'),

        }


class RegUlangForm(forms.ModelForm):
    class Meta:
        model = RegUlang
        fields = '__all__'
