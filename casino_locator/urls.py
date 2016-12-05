from django.conf.urls import include, url
from django.contrib import admin

from casino_finder import views
from doctor_module import views
from rest_framework.urls import template_name

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^system_login/', include(admin.site.urls)),
    url(r'^',include('auth_module.urls')),
    url(r'^',include('casino_finder.urls')),
    url(r'^',include('doctor_module.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
