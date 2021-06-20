from django.urls import path
from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^pesan_pelaporan/$', views.pesan_pelaporan, name="pelaporan"),
    url(r'^laporan_berhasil/$', views.Laporan_berhasil, name="berhasil"),
]
