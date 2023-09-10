#from django.shortcuts import render
#from .models import Freelancer
#from django.http import HttpResponse

# Create your views here.

#def home(request):

 #   searchTerm=request.GET.get('searchFreelancer')
  #  return render(request, "home.html", {'searchTerm': searchTerm})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Freelancer, User
from .models import Schedule
from django.http import JsonResponse
from . forms import freelancerRegistrationForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
                'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'step1.html',
            {'form':CustomUserCreationForm, 'error':'Passwords do not match'})




def registration_step2(request):
    
    user_id = request.session["user_id"]
    
    if not user_id:
        return redirect('registration_step1')
    
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = freelancerRegistrationForm(request.POST)
        if form.is_valid():
            freelancer_form = form.save(commit=False)
            freelancer_form.idfreelancer = user
            freelancer_form.imageprofile = 'agendameproject\static\images\default-avatar-profile.jpg'
            freelancer_form.imagejobs = 'agendameproject\static\images\default-image-5-1.jpg'
            freelancer_form.address = 'The freelancer have not a address'
            freelancer_form.save()
            return redirect('registration_complete')
    else:
        form = freelancerRegistrationForm()

    return render(request, 'step2.html', {'form': form})



def registration_complete(request):
    return render(request, "confirmation.html")



def calendar(request):
    all_events = Schedule.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'schedule.html',context)

def all_events(request):                                                                                                 
    all_events = Schedule.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.title,                                                                                         
            'id': event.id,                                                                                              
            'start': event.starttme.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.endtime.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               

    return JsonResponse(out, safe=False)  

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Schedule(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Schedule.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Schedule.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def detail(request, freelancer_id):
    freelancer = get_object_or_404(Freelancer,pk=freelancer_id)
    return render(request, 'detail.html',{'freelancer':freelancer })


def filter_category(request, category):
    filter_category = Freelancer.objects.filter(category=category)
    return render(request, 'home.html', {'filter_services': filter_category})



