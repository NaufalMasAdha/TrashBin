from django.urls import path
from django.conf.urls import url
from .import views

app_names='accounts'

urlpatterns= [
    url(r'^sign_up/$', views.sign_upview, name="signup"),
    url(r'^sign_in/$', views.sign_inview, name="signin"),
    url(r'^sign_out/$', views.sign_outview, name="signout"),
]
