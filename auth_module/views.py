from django.shortcuts import render,redirect
from auth_module.forms import *
from django.contrib.auth import authenticate,login
from .msg import *
from mpl_toolkits.gtktools import error_message
from json.decoder import errmsg
# Create your views here.


def user_registration(request):
    template_name = 'pages/registration.html'
    errmsg = 'err_msg'
    
    form = UserForm(request.POST or None)
    
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
               login(request,user)
               return redirect('/login/')
            else:
               return render(request, template_name,{errmsg:err_msg['auth_fail']})
            
    else:
        return render(request, template_name,{'form':form}) 
    
    
def user_login(request):
    template_name = 'pages/login.html'
    err_msg = 'err_msg'
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active():
                login(request,user)
                return render(request, template_name, {errmsg:err_msg['auth_success']})
            else:
                return render(request, template_name, {errmsg:err_msg['auth_fail']})
            
    return render(request, template_name) 

def user_logout(request):
    pass