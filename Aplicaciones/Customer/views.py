from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from . forms import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from Aplicaciones.Freelancer.models import User,Request, Events


# Create your views here.

def search(request):
    return HttpResponse('hello there')

def solicitud(request,idfreelancer):

    freelancer = get_object_or_404(Freelancer,pk=idfreelancer)
    print(freelancer.idfreelancer)

    all_events = Events.objects.filter(idfreelancer=freelancer.idfreelancer)

    events=[]
    for event in all_events:  
        print(event)                                                                                           
        events.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start,                                                         
            'end': event.end,                                                            
        })
        print(event.start)
        print(event.end)                                                                                                          
            
    
    horas = []
    for e in range(0,25):
        horas.append(e)

    if request.method == "POST":
        form = requestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Solicitud guardada correctamente!!!")
    else:
        
        form = requestForm(initial={'idfreelancer': freelancer})
        
    
    return render(request, 'solicitud.html', {'form': form,'freelancer':freelancer,'horas':horas,'events':events})

def registration_step1_(request):
    if request.method == 'GET':
        return render(request, 'step1_.html',
            {'form': CustomUserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                
                customers_group = Group.objects.get(name='Customers')
                user.groups.add(customers_group)
                
                user.save()
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('registration_step2_')
            except IntegrityError:
                return render(request, 'step1_.html',
                {'form':CustomUserCreationForm,
                'error':'Nombre de usuario tomado. Escoge un nuevo nombre de usuario'})
        else:
            return render(request, 'step1_.html',
            {'form':CustomUserCreationForm, 'error':'Las contraseñas no coinciden'})



def registration_step2_(request):
    neighborhood= Neighborhood.objects.get(pk=1)
    user_id = request.session["user_id"]
    
    if not user_id:
        return redirect('registration_step1_')
    
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        
        form = customerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            customer_form = form.save(commit=False)
            customer_form.idcustomer = user
            customer_form.idneighborhood = neighborhood
            customer_form.address = 'The customer have not a address'
            customer_form.save()
            return redirect('registration_complete_')
    else:
        form = customerRegistrationForm()

    return render(request, 'step2_.html', {'form': form})



def registration_complete_(request):
    return render(request, "confirmation_.html")


def login_customer_(request):
    if request.method == 'GET':
        return render(request, 'login_.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
    if user is None:
        return render(request,'login_.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
    else:
        login(request, user)
    return redirect('profile')


@login_required
def logout_customer(request):
    logout(request)
    return redirect('home')


@login_required
def profile_(request):
    return render(request, "profile_.html")


@login_required
def edit_profile(request):
    user_id = request.user.id
    customer = User.objects.filter(id=user_id).first()
    form = customerEditForm(instance=customer)
    return render(request, 'edit-profile_.html', {"form":form, 'customer': customer})


def update_profile_(request):
    customer = request.user.customer
    form = customerEditForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():
        form.save()
        
    return render (request, "profile_.html")
