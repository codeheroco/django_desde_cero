from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	(r'^articulos/', include('blog.urls')),
    # Examples:
    # url(r'^$', 'PrimerBlog.views.home', name='home'),
    # url(r'^PrimerBlog/', include('PrimerBlog.foo.urls')),
    url(r'^$', 'blog.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^crear/', 'blog.views.crear', name='crear'),
)
