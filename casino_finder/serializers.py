from rest_framework import serializers
from django.contrib.auth.models import User, Group

from . import models



class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CasinoModel
        fields = ('id','name','address')
#         
#         
# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CityModel
#         fields  = ('id','name')
#         
#         
# class DegreeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DegreeModel
#         fields  = ('id','title','institute_name','instititute_location','status')
#         
#         
# class DesignationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DesignationModel
#         fields  = ('id','title','institute_name','instititute_location','status')
#         
#         
# class HospitalINFSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.HospitalINFModel
#         fields  = ('id','title','location','status')
#         
#         
# class SpecialistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.SpecialistModel
#         fields  = ('id','title','institute_name','instititute_location','status')
#                    
#         
# class DoctorBioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DoctorBioModel
#         fields  = ('id','name','picture','telephone_no','available_time','specialist_ids',
#                    'designation_ids','degree_ids','present_organization_ids')
#         
#         
#         
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
# 
# 
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name') 
