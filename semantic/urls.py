from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from semantic import views

urlpatterns = [
    url(r'^resources/$', views.ResourceList.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/$', views.ResourceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
