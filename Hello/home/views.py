from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime 
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
   
   return render(request,"about.html")
   
    
def gtav(request): 
    return render(request, 'services.html')

def saveEnquiry(request):
    
    return render(request,'contact.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # print("========================================================")
        
        # print(name)
        # print(email)
        # print(phone)
        # print(desc)
        

        # ec = contact(name,email,phone,desc,datetime.today())
        ec = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())

        ec.save()
        messages.success(request,"We will contact you soon")
    return render(request,'contact.html')


def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        name1 = request.POST['name1']
        email1 = request.POST['email1']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request," username must me under 10 chracters")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request," password do not match")
            return redirect('home')

        myuser = User.objects.create_user(username,email1,pass1)
        myuser.get_full_name=name1
        myuser.save()
        messages.success(request, " Account Created Successfully")
        return redirect('/')

def handlelogin(request):
    if request.method =="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, " logged in Successfully")
            return redirect('home')
        else:messages.error(request," invalid Username and Password")
        return redirect('home')

    
        
        
    return HttpResponse('404- Not Found')


def handlelogout(request):
        logout(request)
        messages.success(request," SUCCESS! Successfully Logged Out")
        return redirect('home')


    # return HttpResponse('handlelogout')   

def gow(request):
    return render(request, 'gow.html')
def spider(request):
    return render(request, 'spider.html')
def pubg(request):
    return render(request, 'pubg.html')
def forza(request):
    return render(request, 'forza.html')
def minecraft(request):
    return render(request, 'minecraft.html')