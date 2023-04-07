from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import admin_only,unauthenticated_user,allowed_user
from car.models import CarDetail
from django.template.loader import render_to_string  

from django.core.mail import send_mail


@admin_only
def Index(request):
    product =CarDetail.objects.all()
    context = {
        "product":product
    }
    
    return render(request,'index.html',context)

@allowed_user
def AdminIndex(request):

    return render(request,"admin/adminhome.html")

@unauthenticated_user
def SignIn(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username = username ,password = password)

        if user is not None:
            login(request,user)
            return redirect('Index')
        else:
            messages.info(request,"Username or Password incorrect")
            return redirect('SignIn')
    return render(request,'login.html')

@unauthenticated_user
def SignUp(request):
    form = UserAddForm()
    if request.method =="POST":
        form = UserAddForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            if User.objects.filter(username = username).exists():
                messages.info(request,"User Name Already exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"email Already exists")
                return redirect('SignUp')
            else:
                user = form.save(commit=False)  
                
                user.save()
          
                messages.success(request,"User Created")
              
                return redirect('SignIn')


    context = {"form":form}
    return render(request,'register.html',context)

def SignOut(request):
    logout(request)
    return redirect('Index')

def log(request,pk):
    user=User.objects.get(id=pk)
    check=user.is_active
    context ={
        'check':check
    }

    return render(request,'log.html',context)

def activate(request,pk):
    user=User.objects.get(id=pk)
    user.is_active = True
    user.save()  

    return redirect('SignIn')
# Create your views here.
