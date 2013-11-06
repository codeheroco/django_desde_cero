from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^todos/$', 'blog.views.articulos'),
	url(r'^obtener/(?P<articulo_id>\d+)/$', 'blog.views.articulo'),
	url(r'^agregar_comentario/(?P<articulo_id>\d+)/$', 'blog.views.agregar_comentario'),
)
