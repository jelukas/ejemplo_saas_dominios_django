from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^paginas/$', 'blog.views.paginas', name='paginas'),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.ver_pagina', name='ver_pagina'),
)
