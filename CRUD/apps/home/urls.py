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
    #url(r'^db/(?P<id_db>[0-9]+)/del-table/(?P<table_name>[\w]+)$', 'delete_table', name="del_table"),
    #url(r'^db/(?P<id_db>[0-9]+)/update-table-name/$', 'update_table_name', name="update_table_name"),
    #url(r'^db/(?P<id_db>[0-9]+)/inspectdb/$', 'inspectdb', name="inspectdb"),
    #url(r'^db/(?P<id_db>[0-9]+)/cancel/$', 'close_db', name="close_db"),
)