# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


from tastypie.api import Api
from django.contrib import admin
admin.autodiscover()

from wedding.resource import *
v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
v1_api.register(DisplayResource())
v1_api.register(VendorResource())


# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
                       url(r'^$',
                           TemplateView.as_view(
                               template_name='pages/home.html'),
                           name="home"),
                       url(r'^about/$',
                           TemplateView.as_view(
                               template_name='pages/about.html'),
                           name="about"),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # User management
                       url(r'^users/',
                           include("users.urls",
                                   namespace="users")),
                       url(r'^accounts/', include('allauth.urls')),

                       # Uncomment the next line to enable avatars
                       url(r'^avatar/', include('avatar.urls')),


                       url(r'^api/', include(v1_api.urls)),
                       url(r'^wedd/', 'wedding.views.detail'),
                       # url(r'^view/', 'wedding.views.current_datetime'),


                       # Your stuff: custom urls go here

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
