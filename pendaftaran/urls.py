from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'landing'}, name='logout'),
    url(r'^dashboard/$', views.ppdb, name='ppdb'),
    url(r'^pendaftar/list/$', views.pendaftar_list, name='pendaftar_list'),
    url(r'^pendaftar/tambah/$', views.pendaftar_new, name='pendaftar_new'),
    url(r'^pendaftar/RegistrastiUlang/$', views.input_regulang, name='input_regulang'),
    url(r'^pendaftar/(?P<pk>\d+)/edit/$', views.pendaftar_edit, name='pendaftar_edit'),
    url(r'^pendaftar/(?P<pk>\d+)/detail/$', views.pendaftar_detail, name='pendaftar_detail'),
    url(r'^pendaftar/(?P<pk>\d+)/hapus/$', views.pendaftar_delete, name='pendaftar_delete'),
    url(r'^pendaftar/(?P<pk>\d+)/cetak/$', views.print_pendaftar, name='print_pendaftar'),
    url(r'^daftar_ulang/$', views.daftar_ulang, name='daftar_ulang'),
    url(r'^export/csv/$', views.export_pendaftar, name='export_pendaftar'),
    url(r'^export/csv_cbt/$', views.export_cbt, name='export_cbt'),
    url(r'^export/csv_nilai/$', views.export_pendaftar_nilai, name='export_pendaftar_nilai'),
    url(r'^pendaftar/export/$', views.export_page, name='export_page'),

]
