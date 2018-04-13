# Tutorial from: https://www.merixstudio.com/blog/django-crispy-forms-what-are-they-about/

from django import forms
from .models import Pendaftar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, Field, TabHolder, Tab


class PendaftarForm(forms.ModelForm):
    class Meta:
        model = Pendaftar
        fields = '__all__'
        exclude = {'nomor_pendaftaran', 'password_pendaftaran',}
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

    def __init__(self, *args, **kwargs):
        super(PendaftarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'form-pendaftar'
        self.helper.form_show_labels = True
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_form'
        # self.helper.add_input(Submit('submit', 'Daftar!'))
        self.helper.layout = Layout(
            Fieldset(
                'Data Pendaftar',
                Div(
                    'nama',
                    'jenis_kelamin',
                    'tempat_lahir',
                    Field('tanggal_lahir', placeholder="DD-MM-YYYY misal: 21-10-2001"),
                    'agama_anak',
                    'anak_ke',
                    'jumlah_saudara_kandung',
                    'asal_sekolah',
                    css_class='col-md-4 col-md-offset-4'),
            ),
            Fieldset(
                'Data Orang Tua',
                Div(
                    'nama_ayah',
                    'nama_ibu',
                    'pendidikan_ayah',
                    'pendidikan_ibu',
                    'pekerjaan_ayah',
                    'pekerjaan_ibu',
                    'agama_ayah',
                    'agama_ibu',
                    'alamat_orang_tua',
                    Field('no_telepon', placeholder="08x-xxx-xxx-xxx"),
                    css_class='col-md-4 col-md-offset-4'
                ),
            ),
            Fieldset(
                'Data Wali*)',
                Div('nama_wali',
                    'pendidikan_wali',
                    'agama_wali',
                    'alamat_wali',
                    css_class='col-md-4 col-md-offset-4')
            ),
            Fieldset(
                'Data Nilai',
                HTML("""
                    <table class="table table-striped">
                <thead class="">
                    <tr class="">
                        <th class="">Kelas</th>
                        <th class="">Mapel</th>
                        <th class="">Gasal</th>
                        <th class="">Genap</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="">
                        <td rowspan="3" class="">Kelas 4</td>
                        <td class="">B. Indonesia</td>
                        <td class="">{{ form.indo_kelas4_smt1 }}</td>
                        <td class="">{{ form.indo_kelas4_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td class="">Matematika</td>
                        <td class="">{{ form.mtk_kelas4_smt1 }}</td>
                        <td class="">{{ form.mtk_kelas4_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td class="">IPA</td>
                        <td class="">{{ form.ipa_kelas4_smt1 }}</td>
                        <td class="">{{ form.ipa_kelas4_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td rowspan="3" class="">Kelas 5</td>
                        <td class="">B.Indonesia</td>
                        <td class="">{{ form.indo_kelas5_smt1 }}</td>
                        <td class="">{{ form.indo_kelas5_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td class="">Matematika</td>
                        <td class="">{{ form.mtk_kelas5_smt1 }}</td>
                        <td class="">{{ form.mtk_kelas5_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td class="">IPA</td>
                        <td class="">{{ form.ipa_kelas5_smt1 }}</td>
                        <td class="">{{ form.ipa_kelas5_smt2 }}</td>
                    </tr>
                    <tr class="">
                        <td rowspan="3" class="">Kelas 6</td>
                        <td class="">B.Indonesia</td>
                        <td class="">{{ form.indo_kelas6_smt1 }}</td>
                        </tr>
                    <tr class="">
                        <td class="">Matematika</td>
                        <td class="">{{ form.mtk_kelas6_smt1 }}</td>
                        </tr>
                    <tr class="">
                        <td class="">IPA</td>
                        <td class="">{{ form.ipa_kelas6_smt1 }}</td>
                        </tr>
                </tbody>
            </table>"""),
                css_class=""
            )
        )
