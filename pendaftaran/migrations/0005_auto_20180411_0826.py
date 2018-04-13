# Generated by Django 2.0.2 on 2018-04-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0004_auto_20180410_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendaftar',
            name='agama_anak',
            field=models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katholik', 'Katholik'), ('Hindu', 'Hindhu'), ('Budha', 'Budha'), ('-', '-')], default='islam', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftar',
            name='agama_ayah',
            field=models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katholik', 'Katholik'), ('Hindu', 'Hindhu'), ('Budha', 'Budha'), ('-', '-')], default='islam', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftar',
            name='agama_ibu',
            field=models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katholik', 'Katholik'), ('Hindu', 'Hindhu'), ('Budha', 'Budha'), ('-', '-')], default='islam', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftar',
            name='agama_wali',
            field=models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katholik', 'Katholik'), ('Hindu', 'Hindhu'), ('Budha', 'Budha'), ('-', '-')], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftar',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'L'), ('Perempuan', 'P')], default='laki-laki', max_length=10),
        ),
        migrations.AlterField(
            model_name='pendaftar',
            name='tanggal_lahir',
            field=models.DateField(null=True),
        ),
    ]