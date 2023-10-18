from django import forms
from Aplicaciones.Freelancer.models import Freelancer, Request, Customer

class requestForm(forms.ModelForm):
   
    idfreelancer = forms.ModelChoiceField(queryset=Freelancer.objects.all(), widget = forms.HiddenInput(),label="Freelancer")
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
                'requestday',
                'requesttime',
                'address',
                'phone',
                ]