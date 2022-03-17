from datetime import datetime
from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
def index(request):
      context={
            'variable1':"vivek kumar prajapati is great person",
            'variable2':"vivek kumar prajapati is great person"
      }
      messages.success(request,"this is test message")
      return render(request,'index.html',context)

def about(request):
      return render(request,'about.html')
     
def service(request):
      return render(request,'service.html')
def contact(request):
      if request.method== "POST":
            name = request.POST.get ('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get ('desc')
            contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
            contact.save()
            messages.success(request, 'your message has been sent !')
      return render(request,'contact.html')