from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
	url(r'^$', 'blog.views.home', name='home'),
	url(r'^contacto/$', 'blog.views.contacto', name='contacto'),
	url(r'^conversor/$', 'blog.views.conversor', name='conversor'),
	url(r'^calcu/$', 'blog.views.calcu', name='calcu'),
	url(r'^crono/$', 'blog.views.crono', name='crono'),
	url(r'^curriculum/$', 'blog.views.curriculum', name='curriculum'),
	url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
	#url(r'^mensaje/$', 'blog.views.mensaje', name='mensaje'),
	url(r'^contacto/$', 'blog.views.contacto', name='contacto'),
	url(r'^comentar/$', 'blog.views.comentar', name='comentar'),
)
