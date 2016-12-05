from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
from .models import *
from .serializers import *



@api_view(['GET','POST'])
def doctor_list(request):
    """
    List all doctors and related functionality
    """
    try:
        data = DoctorBioModel.objects.all()
    except DoctorBioModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer = DoctorBioSerializer(data,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer = DoctorBioSerializer(DoctorBioModel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET','PUT','DELETE'])
def doctor_details(request,pk=None):
    """
    List all doctors and related functionality
    """
    try:
        data = DoctorBioModel.objects.get(pk=pk)
    except DoctorBioModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer = DoctorBioSerializer(data,many=True)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer = DoctorBioSerializer(DoctorBioModel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=="DELETE":
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# 
# class ListCreateCasinos(generics.ListCreateAPIView):
#     queryset = CasinoModel.objects.all()
#     serializer_class = CasinoSerializer
#     
#     
# class ListCreateCity(generics.ListCreateAPIView):
#     queryset = CityModel.objects.all()
#     serializer_class = CitySerializer
# 
# class ListCreateDegree(generics.ListCreateAPIView):
#     queryset = DegreeModel.objects.all()
#     serializer_class = DegreeSerializer
#     
# class ListCreateDesignation(generics.ListCreateAPIView):
#     queryset = DesignationModel.objects.all()
#     serializer_class = DesignationSerializer
# 
# class ListCreateSpecialist(generics.ListCreateAPIView):
#     queryset = SpecialistModel.objects.all()
#     serializer_class = SpecialistSerializer
# 
# class ListCreateHospitalINF(generics.ListCreateAPIView):
#     queryset = HospitalINFModel.objects.all()
#     serializer_class = HospitalINFSerializer  
#     
#     
# class ListCreateDoctorBio(generics.ListCreateAPIView):
#     queryset = DoctorBioModel.objects.all()
#     serializer_class = DoctorBioSerializer   
    
# class UserViewSet(generics.ListCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
# 
# 
# class GroupViewSet(generics.ListCreateAPIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

