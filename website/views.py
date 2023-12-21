from django.shortcuts import render,redirect
from .import models
from .models import Contact
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages

def home_page(request):
    return render(request,'home.html')

def img_page(request):
    return render(request,'img.html')



def index_page(request):
    return render(request,'index.html')


def about_us(request):
    return render(request,'about.html')


def contact_us(request):
    a = models.Contact.objects.all()
    context={'form':a}
    if request.method == 'POST':
        x= models.Contact(
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        contact=request.POST.get('contact'),
        subject=request.POST.get('subject'),
        message=request.POST.get('message'),)
        if x is not None:
            x.save()

    return render(request,'contact.html',context)


def our_vision(request):
    return render(request,"our_vision.html")

def rights(request):
    return render(request,"rights.html")


def team(request):
    return render(request,"team.html")


def crud(request):
    return render(request,'crud.html')



def loginpage(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user=user)
            return redirect('read')
    return render(request,'login.html')


# def logout(request):
#     data = Contact.objects.all()
#     data.logout()
#     return render(request,'logout.html')



@login_required(login_url='loginpage')
def read(request):
    data =Contact.objects.all()
    context = {'data':data}
    return render(request,'read.html',context)


def update(request,pk):
    data = Contact.objects.get(pk=pk)
    context = {'data': data}
    if request.method == "POST":
        data.name = request.POST.get('name')
        data.email = request.POST.get('email')
        data.contact = request.POST.get('contact')
        data.subject = request.POST.get('subject')
        data.message = request.POST.get('message')
        data.status = request.POST.get('status')
        data.comment = request.POST.get('comment')
        data.save()
        return redirect('read')
    return render(request, 'update.html', context)


def delete(request,pk):
    data=Contact.objects.get(pk=pk)
    data.delete()
    return redirect('read')


def logout_user(request):
    context = {}
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, 'login.html', context)
