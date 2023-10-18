from django import forms
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile



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


""" class userEditForm(forms.ModelForm):
    email= forms.EmailField(required=False, label="Correo electronico")
    username= forms.CharField(max_length=250, required=False, label="Nombre de usuario")
    
    class Meta:
        model = User
        fields = [
            'email',
            'username',
        ]
"""



class freelancerEditForm(forms.ModelForm):
    phone = forms.IntegerField(label="Numero de telefono")
    idcity = forms.ModelMultipleChoiceField(queryset=City.objects.all(), label="Ciudades", required=False)
    description = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(), label="Descripción")
    imageprofile = forms.ImageField(required=False, label="Imagen de perfil")
    imagejobs = forms.ImageField(required=False, label = "Fotos de trabajos previos")
    idservices = forms.ModelChoiceField(queryset=Service.objects.all(), label="Servicio ofrecido", required=False)
    
    
    class Meta:
        model = Freelancer
        fields = [
                'phone',
                'idcity',
                'description',
                'imageprofile',
                'imagejobs',
                'idservices',
                ]


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = {'date','startime','endtime'}
        labels = {
            "date": ("Fecha"),
            "startime": ("Hora Inicio"),
            "endtime": ("Hora Fin")
        }
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'startime':forms.TimeInput(
                attrs={'type': 'time', 'placeholder': 'H:M', 'class': 'form-control'}),
            'endtime':forms.TimeInput(
                attrs={'type': 'time', 'placeholder': 'H:M', 'class': 'form-control'}), 
        }



class freelancerRegistrationForm(forms.ModelForm):
    
    idfreelancer = forms.IntegerField(widget=forms.HiddenInput(), required=False, label="User")
    idcard = forms.IntegerField(label="Cedula")
    name  = forms.CharField(max_length=250, label="Nombre")
    lastname = forms.CharField(max_length=250, label="Apellidos")
    phone = forms.IntegerField(label="Numero de telefono")
    birthday = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    idcountry = forms.ModelChoiceField(queryset=Country.objects.all() , label="Pais")
    idcity = forms.ModelMultipleChoiceField(queryset=City.objects.all(), label="Ciudades", widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    idneighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all(), required=False, widget=forms.HiddenInput())
    description = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(), label="Descripción")
    imageprofile = forms.ImageField(required=False, label="Imagen de perfil")
    imagejobs = forms.ImageField(required=False, label = "Fotos de trabajos previos")
    address =  forms.CharField(widget=forms.HiddenInput(), required=False)
    idservices = forms.ModelChoiceField(queryset=Service.objects.all(), label="Servicio ofrecido")
    
    
    
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
            'description',
            'imageprofile',
            'imagejobs',
            'address',
            'idservices',
        ]