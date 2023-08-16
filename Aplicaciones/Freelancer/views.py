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



def home(request):

    searchTerm = request.GET.get('searchFreelancer')
    if searchTerm:
        freelancers = Freelancer.objects.filter(nameFreelancer__icontains=searchTerm)
    else:
        freelancers = Freelancer.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'freelancers' :freelancers})
