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


def home(request):

    searchTerm = request.GET.get('searchFreelancer')
    if searchTerm:
        freelancers = Freelancer.objects.filter(nameFreelancer__icontains=searchTerm)
    else:
        freelancers = Freelancer.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'freelancers' :freelancers})

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


