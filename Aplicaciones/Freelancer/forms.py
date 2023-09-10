from django import forms
from . models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass




class freelancerRegistrationForm(forms.ModelForm):
    
    idfreelancer = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    idcard = forms.IntegerField()
    name  = forms.CharField(max_length=250)
    lastname = forms.CharField(max_length=250)
    phone = forms.IntegerField()
    birthday = forms.DateField()
    idcountry = forms.ModelChoiceField(queryset=Country.objects.all())
    idcity = forms.ModelChoiceField(queryset=City.objects.all())
    idneighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all())
    imageprofile = forms.ImageField(widget=forms.HiddenInput(), required=False)
    imagejobs = forms.ImageField(widget=forms.HiddenInput(), required=False)
    address =  forms.CharField(widget=forms.HiddenInput(), required=False)
    idservices = forms.ModelChoiceField(queryset=Services.objects.all())
    
    
    
    class Meta:
        model = Freelancer
        fields = [
            'idfreelancer',
            'idcard',
            'name',
            'lastname',
            'birthday',
            'phone',
            'idcountry',
            'idcity',
            'idneighborhood',
            'imageprofile',
            'imagejobs',
            'address',
            'idservices',
        ]

