from django.conf.urls import include, url


from auth_module.views import *

urlpatterns = [
    # Examples:
#     url(r'^/', include('casino_finder.urls')),
    url(r'^registration/$', user_registration, name='user_registration'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^logout/$', user_logout, name='user_logout'),
]
