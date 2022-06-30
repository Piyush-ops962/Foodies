from django.shortcuts import render,HttpResponse,redirect
from datetime  import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        "variable1":"this is sent",
         "variable2":"Hey boi"
    }
   
    return render(request,'index.html',context)

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')    


def services(request):
   return render(request,'services.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
   # return HttpResponse("this is contact page")