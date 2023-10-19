from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from Aplicaciones.Freelancer.models import Freelancer, Request, Customer
from . forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from Aplicaciones.Freelancer.models import *


class requestForm(forms.ModelForm):
    idfreelancer = forms.ModelChoiceField(queryset=Freelancer.objects.all(), widget = forms.HiddenInput(),label="Freelancer")
    idcustomer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget = forms.HiddenInput(),label="Customer", required=False)
    # CHOICES = [
    #     ('1', 'Option 1'),
    #     ('2', 'Option 2'),
    # ]
    # like = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CHOICES, 
    # )
    requestday = forms.DateField(label="Fecha de solicitud", widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    requesttime = forms.TimeField(label= "Hora de solicitud", widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': 'H:M', 'class': 'form-control'}))
    address = forms.CharField(label='Dirección')
    phone = forms.CharField(label="Teléfono")

    class Meta:
        model = Request
        fields = [
                'idfreelancer',
                'idcustomer',
                'requestday',
                'requesttime',
                'address',
                'phone',
                ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
            model = User
            fields = [
                'username',
                'email',
            ]
            
            labels = {
            'username': ('Nombre de usuario'),
            'email': ("Correo Electronico"),
            }
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
        
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'



class customerEditForm(forms.ModelForm):
    phone = forms.IntegerField(label="Numero de telefono")
    idcity = forms.ModelMultipleChoiceField(queryset=City.objects.all(), label="Ciudades", required=False)
    description = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(), label="Descripción")
    imageprofile = forms.ImageField(required=False, label="Imagen de perfil")
    imagejobs = forms.ImageField(required=False, label = "Fotos de trabajos previos")

    
    
    class Meta:
        model = Customer
        fields = [
                'phone',
                'idcity',
                'imageprofile',
                ]



class customerRegistrationForm(forms.ModelForm):
    
    idcustomer = forms.IntegerField(widget=forms.HiddenInput(), required=False, label="User")
    idcard = forms.IntegerField(label="Cedula")
    name  = forms.CharField(max_length=250, label="Nombre")
    lastname = forms.CharField(max_length=250, label="Apellidos")
    phone = forms.IntegerField(label="Numero de telefono")
    birthday = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    idcountry = forms.ModelChoiceField(queryset=Country.objects.all() , label="Pais")
    idcity = forms.ModelChoiceField(queryset=City.objects.all(), label="Ciudad", widget=forms.Select(attrs={'class': 'form-control'}))
    idneighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all(), required=False, widget=forms.HiddenInput())
    imageprofile = forms.ImageField(required=False, label="Imagen de perfil")
    address =  forms.CharField(widget=forms.HiddenInput(), required=False)

    
    class Meta:
        model = Customer
        fields = [
            'idcustomer',
            'idcard',
            'name',
            'lastname',
            'birthday',
            'phone',
            'idcountry',
            'idcity',
            'idneighborhood',
            'imageprofile',
            'address',
        ]
        
