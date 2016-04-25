from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list_and_groups, name='post_list_and_groups'),
    url(r'(?P<pk>\d+)/$',views.groups, name = 'grupos'),
    url(r'^nuevo_grupo/$', views.nuevo_grupo, name='nuevo_grupo'),
    url(r'^registro/$', views.registro, name = 'registro'),
    
]