from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('CRUD.apps.home.urls')),
    #url(r'^home/', include('home.urls',namespace='home')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^captcha/', include('captcha.urls')),
    #url(r'^', include('password_reset.urls')),

	url(r'^contrasena/restablecer/$', 'django.contrib.auth.views.password_reset', name = 'recuperar'),
    url(r'^contrasena/restablecer/enviada/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^contrasena/restablecer/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^contrasena/restablecer/completo/$', 'django.contrib.auth.views.password_reset_complete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

