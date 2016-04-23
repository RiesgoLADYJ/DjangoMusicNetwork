from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list_and_groups, name='post_list_and_groups'),
]