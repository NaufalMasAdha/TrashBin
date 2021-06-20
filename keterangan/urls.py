from django.urls import path
from django.conf.urls import url
from .import views

app_name='keterangan'
urlpatterns = [
    url(r'^$', views.keterangan_list, name="list"),
    url(r'^peta_baiturrahman/$', views.peta_baiturrahman),
    url(r'^peta_banda_raya/$', views.peta_banda_raya),
    url(r'^peta_jaya_baru/$', views.peta_jaya_baru),
    url(r'^peta_kuta_alam/$', views.peta_kuta_alam),
    url(r'^peta_kuta_raja/$', views.peta_kuta_raja),
    url(r'^peta_lueng_bata/$', views.peta_lueng_bata),
    url(r'^peta_muraxa/$', views.peta_meuraxa),
    url(r'^peta_syiah_kuala/$', views.peta_syiah_kuala),
    url(r'^peta_ulee_kareng/$', views.peta_ulee_kareng),
]
