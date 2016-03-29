from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^engineering/$', views.engineering ,name ='engineering'),
    url(r'^medical/$', views.medical ,name ='medical'),
    url(r'^bpharm /$', views.bpharm ,name ='bpharm '),
    url(r'^commerce2/$', views.commerce2 ,name ='commerce2'),
    url(r'^arts1/$', views.arts1 ,name ='arts1'),
    url(r'^arts2/$', views.arts2 ,name ='arts2'),
]
