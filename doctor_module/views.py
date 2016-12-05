from django.contrib.auth import authenticate,login,logout
from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from doctor_module.forms import *
from doctor_module.models import *
from auth_module.msg import *



# Create your views here.
""" Constant varisble here """
HOSPITAL_SEARCH ='lists_hospital'
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    lists = DoctorBioModel.objects.all()
    form = DoctorForm(request.POST or None)
    query = request.GET.get('q')
    
    if query:
        lists = lists.filter(
            Q(name__contains=query) |
            Q(telephone_no__contains=query) |
            Q(available_time__contains=query)
        ).distinct()

        lists= pagination(request, lists=lists)

        return render(request,'doctor/create.html',{'form':form,'lists':lists})

    return render(request,'homepage.html')


def create_doctor(request):
    lists = DoctorBioModel.objects.all()
#     if not request.user.is_authenticated():
#         return render(request, 'pages/login.html')
#     else:
    form = DoctorForm(request.POST or None, request.FILES or None)
    lists = pagination(request, lists=lists)
    if form.is_valid():
        post_data = form.save(commit=False)
        if request.FILES:
            post_data.picture = request.FILES['picture']
            file_type = post_data.picture.url.split('.')[-1]
            file_type = file_type.lower()

            context = {
                'lists': lists,
                'form': form,
            }

            if file_type not in ['png', 'jpg', 'jpeg']:
                context['error_message'] = 'file type is not supprted'

            return render(request,'doctor/create.html',context)

        post_data.save()
        return redirect('create_doctor')
    
    else:
        return render(request,'doctor/create.html',{'form':form,'lists':lists})
    
    
    
def edit_doctor(request,pk=None):
    lists = DoctorBioModel.objects.all()
    instance = get_object_or_404(DoctorBioModel,pk=pk)
    form = DoctorForm(request.POST or None, request.FILES or None, instance=instance)
    lists = pagination(request, lists=lists)

    if request.method=="POST":
        if form.is_valid():
            post_data = form.save(commit=False)
            if request.FILES:
                post_data.picture = request.FILES['picture']
                file_type = post_data.picture.url.split('.')[-1]
                file_type = file_type.lower()

                if file_type not in ['png', 'jpg', 'jpeg']:
                    context = {
                        'lists': lists,
                        'form': form,
                        'error_message': 'file type is not supprted'
                    }

                return render(request, 'doctor/create.html', context)

            post_data.save()
            return redirect('create_doctor')

    return render(request,'doctor/edit.html',{'form':form,'lists':lists,'pk':pk})
    
    
def delete(request,pk):
    instance = get_object_or_404(DoctorBioModel,pk=pk)
    instance.delete()
    return redirect('create_doctor')


""" Hospital information store """

def index_hospital(request):
    lists = HospitalINFModel.objects.all()
    form = HospitalForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(title__contains=query) |
            Q(location__contains=query)
        ).distinct()

    return render(request, 'hospital/create.html', {'form': form, 'lists': lists})



def create_hospital(request):
    lists = HospitalINFModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = HospitalForm(request.POST or None)
    if form.is_valid():
        post_data = form.save(commit=False)
        post_data.save()
        return redirect('create_hospital')

    else:
        context={
            'form': form,
            'lists': lists,
            'HOSPITAL_SEARCH':HOSPITAL_SEARCH
        }
        return render(request, 'hospital/create.html', context)


def edit_hospital(request, pk=None):
    lists = HospitalINFModel.objects.all()
    instance = get_object_or_404(HospitalINFModel, pk=pk)
    form = HospitalForm(request.POST or None, instance=instance)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('create_hospital')

    context = {
        'form': form,
        'lists': lists,
        'pk': pk,
        'HOSPITAL_SEARCH': HOSPITAL_SEARCH
    }
    return render(request, 'hospital/edit.html', context)


def delete_hospital(request, pk):
    print "This is delete function----------------------------"
    instance = get_object_or_404(HospitalINFModel, pk=pk)
    instance.delete()
    return redirect('create_hospital')


""" Specialist information store """

def index_specialist(request):
    lists = SpecialistModel.objects.all()
    form = SpecialistForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(title__contains=query) |
            Q(institute_name__contains=query) |
            Q(instititute_location__contains=query)
        ).distinct()

    return render(request, 'specialist/create.html', {'form': form, 'lists': lists})



def create_specialist(request):
    lists = SpecialistModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = SpecialistForm(request.POST or None)
    if form.is_valid():
        post_data = form.save(commit=False)
        post_data.save()
        return redirect('create_specialist')

    else:
        context={
            'form': form,
            'lists': lists,
            'search': 'lists_specialist'
        }
        return render(request, 'specialist/create.html', context)


def edit_specialist(request, pk=None):
    lists = SpecialistModel.objects.all()
    instance = get_object_or_404(SpecialistModel, pk=pk)
    form = SpecialistForm(request.POST or None, instance=instance)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('create_specialist')

    context = {
        'form': form,
        'lists': lists,
        'pk': pk,
        'search': 'lists_specialist'
    }
    return render(request, 'specialist/edit.html', context)


def delete_specialist(request, pk):
    instance = get_object_or_404(SpecialistModel, pk=pk)
    instance.delete()
    return redirect('create_specialist')



""" Designation information store """

def index_designation(request):
    lists = DesignationModel.objects.all()
    form = DesignationForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(title__contains=query) |
            Q(institute_name__contains=query) |
            Q(instititute_location__contains=query)
        ).distinct()

    return render(request, 'designation/create.html', {'form': form, 'lists': lists})



def create_designation(request):
    lists = DesignationModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = DesignationForm(request.POST or None)
    if form.is_valid():
        post_data = form.save(commit=False)
        post_data.save()
        return redirect('create_designation')

    else:
        context={
            'form': form,
            'lists': lists,
            'search': 'lists_designation'
        }
        return render(request, 'designation/create.html', context)


def edit_designation(request, pk=None):
    lists = DesignationModel.objects.all()
    instance = get_object_or_404(DesignationModel, pk=pk)
    form = DesignationForm(request.POST or None, instance=instance)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('create_designation')

    context = {
        'form': form,
        'lists': lists,
        'pk': pk,
        'search': 'lists_designation'
    }
    return render(request, 'designation/edit.html', context)


def delete_designation(request, pk):
    instance = get_object_or_404(DesignationModel, pk=pk)
    instance.delete()
    return redirect('create_designation')



""" Degree information store """

def index_degree(request):
    lists = DegreeModel.objects.all()
    form = DegreeForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(title__contains=query) |
            Q(institute_name__contains=query) |
            Q(instititute_location__contains=query)
        ).distinct()

    return render(request, 'degree/create.html', {'form': form, 'lists': lists})



def create_degree(request):
    lists = DegreeModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = DegreeForm(request.POST or None)
    if form.is_valid():
        post_data = form.save(commit=False)
        post_data.save()
        return redirect('create_degree')

    else:
        context={
            'form': form,
            'lists': lists,
            'search': 'lists_degree'
        }
        return render(request, 'degree/create.html', context)


def edit_degree(request, pk=None):
    lists = DegreeModel.objects.all()
    instance = get_object_or_404(DegreeModel, pk=pk)
    form = DegreeForm(request.POST or None, instance=instance)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('create_degree')

    context = {
        'form': form,
        'lists': lists,
        'pk': pk,
        'search': 'lists_designation'
    }
    return render(request, 'degree/edit.html', context)


def delete_degree(request, pk):
    instance = get_object_or_404(DegreeModel, pk=pk)
    instance.delete()
    return redirect('create_degree')



""" City information store """

def index_city(request):
    lists = CityModel.objects.all()
    form = CityForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(name__contains=query)
        ).distinct()

    return render(request, 'city/create.html', {'form': form, 'lists': lists})


def create_city(request):
    lists = CityModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = CityForm(request.POST or None)
    if form.is_valid():
        post_data = form.save(commit=False)
        post_data.save()
        return redirect('create_city')

    else:
        context={
            'form': form,
            'lists': lists,
            'search': 'lists_city'
        }
        return render(request, 'city/create.html', context)


def edit_city(request, pk=None):
    lists = CityModel.objects.all()
    instance = get_object_or_404(CityModel, pk=pk)
    form = CityForm(request.POST or None, instance=instance)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('create_city')

    context = {
        'form': form,
        'lists': lists,
        'pk': pk,
        'search': 'lists_city'
    }
    return render(request, 'city/edit.html', context)


def delete_city(request, pk):
    instance = get_object_or_404(CityModel, pk=pk)
    instance.delete()
    return redirect('create_city')




def pagination(request,lists):

    paginator = Paginator(lists,4)
    page= request.GET.get('page')

    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    return lists

    
                