#from django.shortcuts import render
#from .models import Freelancer
#from django.http import HttpResponse

# Create your views here.

#def home(request):

 #   searchTerm=request.GET.get('searchFreelancer')
  #  return render(request, "home.html", {'searchTerm': searchTerm})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Freelancer
from .models import Schedule
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Freelancer
from django.shortcuts import get_object_or_404, redirect


def home(request):

    searchTerm = request.GET.get('searchFreelancer')
    if searchTerm:
        freelancers = Freelancer.objects.filter(nameFreelancer__icontains=searchTerm)
    else:
        freelancers = Freelancer.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'freelancers' :freelancers})

def sign_up(request):
    return render(request, 'sign_up.html')

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



