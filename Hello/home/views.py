from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)
   # return HttpResponse("this is homepage")

def about(request):
      return render(request,'about.html')
    
def services(request):
     return render(request,'services.html')

def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=Contact(name=name,email=email)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')


  