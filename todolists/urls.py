from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_list/$', views.new_list, name='new_list'),
    url(r'^show_lists/$', views.show_lists, name='show_lists'),
    url(r'^list_detail/(?P<pk>\d+)/$', views.list_detail, name='list_detail'),
]