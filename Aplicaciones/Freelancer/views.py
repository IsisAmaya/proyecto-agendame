#from django.shortcuts import render
#from .models import Freelancer
#from django.http import HttpResponse

# Create your views here.

#def home(request):

 #   searchTerm=request.GET.get('searchFreelancer')
  #  return render(request, "home.html", {'searchTerm': searchTerm})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Freelancer, User, Schedule, Neighborhood
from .models import Schedule
from django.http import JsonResponse
from . forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect


def home(request):

    searchTerm = request.GET.get('searchFreelancer')
    if searchTerm:
        freelancers = Freelancer.objects.filter(nameFreelancer__icontains=searchTerm)
    else:
        freelancers = Freelancer.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'freelancers' :freelancers})



def registration_step1(request):
    if request.method == 'GET':
        return render(request, 'step1.html',
            {'form': CustomUserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                
                freelancers_group = Group.objects.get(name='Freelancers')
                user.groups.add(freelancers_group)
                
                user.save()
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('registration_step2')
            except IntegrityError:
                return render(request, 'step1.html',
                {'form':CustomUserCreationForm,
                'error':'Nombre de usuario tomado. Escoge un nuevo nombre de usuario'})
        else:
            return render(request, 'step1.html',
            {'form':CustomUserCreationForm, 'error':'Las contraseñas no coinciden'})



def registration_step2(request):
    neighborhood= Neighborhood.objects.get(pk=1)
    user_id = request.session["user_id"]
    
    if not user_id:
        return redirect('registration_step1')
    
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        
        form = freelancerRegistrationForm(request.POST)
        if form.is_valid():
            freelancer_form = form.save(commit=False)
            freelancer_form.idfreelancer = user
            freelancer_form.idneighborhood = neighborhood
            freelancer_form.address = 'The freelancer have not a address'
            freelancer_form.save()
            return redirect('registration_complete')
    else:
        form = freelancerRegistrationForm()

    return render(request, 'step2.html', {'form': form})



def registration_complete(request):
    return render(request, "confirmation.html")


def login_freelancer(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
    if user is None:
        return render(request,'login.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
    else:
        login(request, user)
    return redirect('profile')


@login_required
def logout_freelancer(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, "perfil.html")


@login_required
def edit_profile(request):
    user_id = request.user.id
    freelancer = User.objects.filter(id=user_id).first()
    form = freelancerEditForm(instance=freelancer)
    return render(request, 'edit-profile.html', {"form":form, 'freelancer': freelancer})


def update_profile(request):
    freelancer = request.user.freelancer
    
    form = freelancerEditForm(request.POST, instance=freelancer)
    if form.is_valid():
        form.save()
        
    return render (request, "perfil.html")


def schedule(request):
    form = ScheduleForm()
    return render(request, 'schedule.html', {'form': form})


def uploadschedule(request):
    idfreelancer = request.user.id
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El calendario fue guardado correctamente!!!")
    else:
        form = ScheduleForm()
    schedules = Schedule.objects.filter(idfreelancer__icontains=idfreelancer)
    return render(request, 'schedule.html', {'form': form,'schedules': schedules})


def deleteShedule(request, idschedule):
    schedule = get_object_or_404(Schedule, pk=idschedule)
    # obtengo el idfreelancer
    idfreelancer = schedule.idfreelancer
    schedule.delete()
    return redirect('/calendarioFreelancer/'+ str(idfreelancer))


def detail(request, freelancer_id):
    freelancer = get_object_or_404(Freelancer,pk=freelancer_id)
    return render(request, 'detail.html',{'freelancer':freelancer })


def filter_category(request, category):
    filter_category = Freelancer.objects.filter(category=category)
    return render(request, 'home.html', {'filter_services': filter_category})



