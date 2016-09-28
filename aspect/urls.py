from django.conf.urls import url
from aspect import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<name>\w+)/(?P<namespace>\w+):(?P<id>\w+)$',views.term,name='term'),
  url(r'^(?P<name>\w+)/$', views.aspect, name='aspect'),
]
