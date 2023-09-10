from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
##print('hola')
##from Freelancer.models import Freelancer

# Create your views here.

def search(request):
    return HttpResponse('hello there')

#def detail(request, freelancer_id):
 #   freelancer = get_object_or_404(Freelancer,pk=freelancer_id)
    ##reviews = Review.objects.filter(movie = movie)
  #  return render(request, 'detail.html',{'freelancer':freelancer })
