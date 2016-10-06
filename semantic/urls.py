from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from semantic import views

urlpatterns = [
    #url(r'^$', views.api_root),
    url(r'^resources/$', views.ResourceList.as_view()),
    url(r'^resources/(?P<pk>.+)/$', views.ResourceDetail.as_view()),
    url(r'^literals/$', views.LiteralList.as_view()),
    url(r'^literals/(?P<pk>[0-9]+)/$', views.LiteralDetail.as_view()),
    url(r'^types/$', views.TypeStatementList.as_view()),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeStatementDetail.as_view()),
    url(r'^assertions/$', views.AssertedStatementList.as_view()),
    url(r'^assertions/(?P<pk>[0-9]+)/$', views.AssertedStatementDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
