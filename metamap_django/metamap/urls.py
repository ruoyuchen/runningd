from django.conf.urls import url

from views import etls, metas

app_name = 'metamap'
urlpatterns = [
    url(r'^$', etls.IndexView.as_view(), name='index'),

    url('etls/list', etls.IndexView.as_view(), name='index2'),
    url(r'^etls/(?P<pk>[0-9]+)/$', etls.edit, name='add'),
    url(r'^etls/blood/(?P<etlid>[0-9]+)/$', etls.blood, name='blood'),
    url(r'^etls/exec/(?P<etlid>[0-9]+)/$', etls.exec_job, name='exec'),

    url('meta/list', metas.IndexView.as_view(), name='index'),
]
