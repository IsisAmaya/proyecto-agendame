from django.shortcuts import render
from .models import Freelancer

# Create your views here.

def home(request):
    return render(request, "FreelancerVisualization.html")