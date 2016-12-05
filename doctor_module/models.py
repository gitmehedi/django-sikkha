from __future__ import unicode_literals

from django.db import models




class CityModel(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
        
class DegreeModel(models.Model):
    title = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=50, blank=True, null=True)
    instititute_location = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title']

class DesignationModel(models.Model):
    title = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=50, blank=True, null=True)
    instititute_location = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        
        
class SpecialistModel(models.Model):
    title = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=50, blank=True, null=True)
    instititute_location = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=["title"]

        

class HospitalINFModel(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        
                
        
class DoctorBioModel(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, null=True,verbose_name='Picture')
    telephone_no = models.IntegerField(verbose_name='Telephone No', )
    available_time = models.IntegerField(verbose_name='Available Time', )
    gender = models.CharField(max_length=30)

    specialist = models.ForeignKey(SpecialistModel,on_delete=models.CASCADE,
                                       verbose_name='Specialist')
    designation = models.ForeignKey(DesignationModel,on_delete=models.CASCADE,
                                        verbose_name='Designation')
    degree = models.ForeignKey(DegreeModel,on_delete=models.CASCADE,
                                   verbose_name='Degree')
    present_organization = models.ForeignKey(HospitalINFModel,on_delete=models.CASCADE,
                                                 verbose_name='Present Organization')

    class Meta:
        ordering=["id"]
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.name
        




