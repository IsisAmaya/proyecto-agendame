from django import forms
from Aplicaciones.Freelancer.models import Freelancer, Request, Customer

class requestForm(forms.ModelForm):

    # def __init__(self,*args,**kwargs):
    #     self.idfreelancer = kwargs.pop('idfreelancer')
    #     super(requestForm,self).__init__(*args,**kwargs)
    #     self.fields['idfreelancer'].widget = forms.TextInput(attrs={'size':idfreelancer})

    # idfreelancer = forms.CharField()

    # idcustomer = forms.ModelChoiceField(queryset=Customer.objects.values_list(), label="Cliente")    
    idfreelancer = forms.ModelChoiceField(queryset=Freelancer.objects.all(), label="Freelancer")
    # idfreelancer = forms.CharField(label='idfreelancer')
    requestday = forms.DateField(label="Fecha de solicitud", widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    requesttime = forms.TimeField(label= "Hora de solicitud", widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': 'H:M', 'class': 'form-control'}))
    # address = forms.ModelChoiceField(queryset=Customer.objects.values_list('address'))
    # phone = forms.ModelChoiceField(queryset=Customer.objects.values_list('phone'))
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
    def __init__(self, freelancer,*args, **kwargs):
        super(requestForm, self).__init__(*args, **kwargs)
        self.freelancer = freelancer
        # self.fields['idfreelancer'] = self.freelancer
        print('hasdha')
        print(self.freelancer)
        print(self.freelancer.name)
        self.fields['idfreelancer'] = Freelancer.objects.filter(idfreelancer=self.freelancer)
        # self.fields['idfreelancer'] = forms.ModelChoiceField(queryset = self.freelancer,label = 'Freelancer')
        # self.fields['idfreelancer'] = forms.ModelChoiceField(queryset = self.freelancer,label = 'Freelancer')
        # forms.ModelChoiceField(queryset=Freelancer.objects.all(), label="Freelancer")
        # self.fields['idfreelancer'].queryset  = Freelancer.objects.filter(idfreelancer=self.freelancer)
        # self.fields['idfreelancer'] = forms.ModelChoiceField(queryset=freelancer, label='Freelancer:')
        
    #     queryset = friends.exclude(id__in=chat_users)
        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None
        #     self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
        