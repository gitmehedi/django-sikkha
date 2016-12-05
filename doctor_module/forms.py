from django import forms
from .models import * 


class DoctorForm(forms.ModelForm):
    GENDER = (
        ('','----Please Select----'),
        ('male', 'Male'),
        ('female','Female')
    )
    telephone_no = forms.CharField(max_length=50)
    available_time = forms.CharField(max_length=50)
    gender = forms.ChoiceField(widget=forms.Select, choices= GENDER)
    picture = forms.FileInput()

    class Meta:
        model = DoctorBioModel
        fields = ['name','picture','gender','telephone_no','available_time','specialist','designation',
                  'degree','present_organization']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = HospitalINFModel
        fields = ['title', 'location', 'status']

class SpecialistForm(forms.ModelForm):
    class Meta:
        model = SpecialistModel
        fields = ['title', 'institute_name','instititute_location', 'status']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = DesignationModel
        fields = ['title', 'institute_name','instititute_location', 'status']

class DegreeForm(forms.ModelForm):
    class Meta:
        model = DegreeModel
        fields = ['title', 'institute_name','instititute_location', 'status']

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = ['name', 'status']