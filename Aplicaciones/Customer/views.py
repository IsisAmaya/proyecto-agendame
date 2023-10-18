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