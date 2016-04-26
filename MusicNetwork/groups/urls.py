from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list_and_groups, name='post_list_and_groups'),
    url(r'(?P<pk>\d+)/$',views.groups, name = 'grupos'),
    url(r'^nuevo_grupo/$', views.nuevo_grupo, name='nuevo_grupo'),
    url(r'^posts/$', views.crearPost, name='posts'),
    url(r'^registro/$', views.registro, name = 'registro'),
    url(r'^login/$', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout'),

]