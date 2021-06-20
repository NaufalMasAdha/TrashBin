from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^keterangan_list/', include('keterangan.urls')),
    url(r'^pelaporan/', include('pelaporan.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^Deskripsi/$', views.about),
    url(r'^$', views.homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^map/$', views.map),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
