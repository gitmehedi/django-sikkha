from django.contrib import admin
from doctor_module.models import *
    
    
    
class CityAdmin(admin.ModelAdmin):
    fields =['name']
    
class DoctorBioAdmin(admin.ModelAdmin):
    fields = ['name', 'picture','telephone_no', 'available_time', 'specialist', 'degree',
              'designation','present_organization']

class HospitalINFAdmin(admin.ModelAdmin):
    fields = ['title','location','status']

class DegreeAdmin(admin.ModelAdmin):
    fields = ['title','institute_name','instititute_location','status']

class DesignationAdmin(admin.ModelAdmin):
    fields = ['title', 'institute_name', 'instititute_location', 'status']

class DSpecialistAdmin(admin.ModelAdmin):
    fields = ['title', 'institute_name', 'instititute_location', 'status']
    

admin.site.register(DoctorBioModel,DoctorBioAdmin)
admin.site.register(HospitalINFModel,HospitalINFAdmin)
admin.site.register(DegreeModel,DegreeAdmin)
admin.site.register(DesignationModel,DesignationAdmin)
admin.site.register(SpecialistModel,DSpecialistAdmin)
admin.site.register(CityModel, CityAdmin)
