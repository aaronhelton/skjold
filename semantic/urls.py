from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from semantic import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^resources/$', views.ResourceList.as_view(), name='resource-list'),
    url(r'^resources/(?P<pk>.+)/$', views.ResourceDetail.as_view(), name='resource-detail'),
    url(r'^literals/$', views.LiteralList.as_view(), name='literal-list'),
    url(r'^literals/(?P<pk>[0-9]+)/$', views.LiteralDetail.as_view(), name='literal-detail'),
    url(r'^types/$', views.TypeStatementList.as_view(), name='type-list'),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeStatementDetail.as_view(), name='type-detail'),
    url(r'^assertions/$', views.AssertedStatementList.as_view(), name='assertion-list'),
    url(r'^assertions/(?P<pk>[0-9]+)/$', views.AssertedStatementDetail.as_view(), name='assertion-detail'),
    url(r'^quotes/$', views.QuotedStatementList.as_view(), name='quote-list'),
    url(r'^quotes/(?P<pk>[0-9]+)/$', views.QuotedStatementDetail.as_view(), name='quote-detail'),
    url(r'^classes/$', views.ClassList.as_view(), name='class-list'),
    url(r'^classes/(?P<pk>.+)/$', views.ClassDetail.as_view(), name='class-detail'),
    url(r'^predicates/$', views.PredicateList.as_view(), name='predicate-list'),
    url(r'^predicates/(?P<pk>.+)/$', views.PredicateDetail.as_view(), name='predicate-detail'),
    url(r'^namespaces/$', views.NamespaceList.as_view(), name='namespace-list'),
    url(r'^namespaces/(?P<pk>[0-9a-zA-Z_]+)/$', views.NamespaceDetail.as_view(), name='namespace-detail'),
    url(r'^contexts/$', views.ContextList.as_view(), name='context-list'),
    url(r'^contexts/(?P<pk>[0-9a-zA-Z_]+)/$', views.ContextDetail.as_view(), name='context-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
