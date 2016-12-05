from django.conf.urls import include, url

from doctor_module import views

urlpatterns = [
    url(r'^doctor/create', views.create_doctor, name='create_doctor'),
    url(r'^doctor/edit/(?P<pk>[0-9]+)/$', views.edit_doctor, name='edit_doctor'),
    url(r'^doctor/delete/(?P<pk>[0-9]+)/$', views.delete, name='delete_doctor'),
    url(r'^hospital/$', views.index_hospital, name='lists_hospital'),
    url(r'^hospital/create/$', views.create_hospital, name='create_hospital'),
    url(r'^hospital/edit/(?P<pk>[0-9]+)/$', views.edit_hospital, name='edit_hospital'),
    url(r'^hospital/delete/(?P<pk>[0-9]+)/$', views.delete_hospital, name='delete_hospital'),
    url(r'^specialist/$', views.index_specialist, name='lists_specialist'),
    url(r'^specialist/create/$', views.create_specialist, name='create_specialist'),
    url(r'^specialist/edit/(?P<pk>[0-9]+)/$', views.edit_specialist, name='edit_specialist'),
    url(r'^specialist/delete/(?P<pk>[0-9]+)/$', views.delete_specialist, name='delete_specialist'),

    url(r'^designation/$', views.index_designation, name='lists_designation'),
    url(r'^designation/create/$', views.create_designation, name='create_designation'),
    url(r'^designation/edit/(?P<pk>[0-9]+)/$', views.edit_designation, name='edit_designation'),
    url(r'^designation/delete/(?P<pk>[0-9]+)/$', views.delete_designation, name='delete_designation'),

    url(r'^degree/$', views.index_degree, name='lists_degree'),
    url(r'^degree/create/$', views.create_degree, name='create_degree'),
    url(r'^degree/edit/(?P<pk>[0-9]+)/$', views.edit_degree, name='edit_degree'),
    url(r'^degree/delete/(?P<pk>[0-9]+)/$', views.delete_degree, name='delete_degree'),

    url(r'^city/$', views.index_city, name='lists_city'),
    url(r'^city/create/$', views.create_city, name='create_city'),
    url(r'^city/edit/(?P<pk>[0-9]+)/$', views.edit_city, name='edit_city'),
    url(r'^city/delete/(?P<pk>[0-9]+)/$', views.delete_city, name='delete_city'),


    
#     url(r'^api/cities', views.ListCreateCity.as_view(), name='city'),
#     url(r'^api/degree', views.ListCreateDegree.as_view(), name='degree'),
#     url(r'^api/designation', views.ListCreateDesignation.as_view(), name='designation'),
#     url(r'^api/specialist', views.ListCreateSpecialist.as_view(), name='specialist'),
#     url(r'^api/hospital', views.ListCreateHospitalINF.as_view(), name='hospital'),
#     url(r'^api/doctors', views.ListCreateDoctorBio.as_view(), name='doctors'),
#     url(r'^api/doctor_lists/$', views.doctor_list, name='doctor_lists'),
#     url(r'^api/doctor_details/(?P<pk>[0-9]+)$', views.doctor_details, name='doctor_details'),
]
