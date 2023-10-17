from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from . forms import *
from django.contrib import messages
from Aplicaciones.Freelancer.models import User,Request, Events


# Create your views here.

def search(request):
    return HttpResponse('hello there')

def solicitud(request,idfreelancer):

    # idcustomer = request.user.customer
    # form = requestForm(request.POST, request.FILES, instance=idcustomer
    # users = request.user.idrequest
    # print(users)
    freelancer = get_object_or_404(Freelancer,pk=idfreelancer)
    # freelancer = Freelancer.objects.all()
    print(freelancer)
    if request.method == "POST":
        form = requestForm(freelancer,request.POST)
        if form.is_valid():
            print('entro a POST')
            form.save()
            messages.success(request, "Solicitud guardada correctamente!!!")
    else:
        form = requestForm(freelancer,request.POST)
    
    return render(request, 'solicitud.html', {'form': form})




