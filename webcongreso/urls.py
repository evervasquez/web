from django.conf.urls import patterns,url
from webcongreso.view import web,presentacion,cronograma,mision_vision,comision_organizadora,costos_vida,contactenos,papers
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webcongreso.views.home', name='home'),
    url(r'^$', web),
    url(r'web/^$', web),
    url(r'^presentacion/$', presentacion),
    url(r'^cronograma/$', cronograma),
    url(r'^mision_vision/$', mision_vision),
    url(r'^comision_organizadora/$', comision_organizadora),
    url(r'^costos_vida/$', costos_vida),
    url(r'^contactenos/$', contactenos),
     url(r'^papers/$', papers),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
