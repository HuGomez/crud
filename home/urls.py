# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from views import *

upload_patterns= patterns(
    '',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        UploadListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        UploadUpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        UploadCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        UploadDeleteView.as_view(),
        name='delete'))


newpatterns = patterns(
    '',
    url(r'^upload/', include(upload_patterns, 
        namespace="upload")))


try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from views import *

upload_patterns= patterns(
    '',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        UploadListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        UploadUpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        UploadCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        UploadDeleteView.as_view(),
        name='delete'))


newpatterns = patterns(
    '',
    url(r'^upload/', include(upload_patterns, 
        namespace="upload")))


try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns
