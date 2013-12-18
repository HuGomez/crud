from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('CRUD.apps.home.views',
	url(r'^$', 'home', name='inicio'),
	url(r'^login/$', 'login_view', name='login'),
	url(r'^logout/$', 'logout_view', name='logout'),
	url(r'^nuevo/$','nuevo_usuario', name='nuevo'),
	url(r'^adminusers/$', 'adminusers', name='adminusers'),
	url(r'^edit/usuario/(?P<usuario>.*)/$', 'editarUsuario', name='edituser'),
    url(r'^delete/usuario/(?P<usuario>.*)/$', 'borrarUsuario', name='deleteuser'),
    url(r'^admintables/$', 'admintables', name='admintables'),
    url(r'^delete/files/$', 'delete', name='delete'),
    url(r'^db/(?P<name>[\w]+)/$', 'personalize', name="personalize"),
)