from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    idcountry = models.AutoField(primary_key=True)
    namecounty= models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.namecounty


class City(models.Model):
    idcity = models.AutoField(primary_key=True)
    namecity= models.CharField(max_length=250)
    idcountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.namecity

class Neighborhood(models.Model):
    idneighborhood = models.AutoField(primary_key=True)
    nameneighborhood= models.CharField(max_length=250)
    idcity = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nameneighborhood

class Service(models.Model):
    idservices= models.AutoField(primary_key=True)
    name= models.CharField(max_length=250)
    description = models.CharField(max_length=900)
    
    def __str__(self) -> str:
        return self.name


""" class User(models.Model):
    iduser= models.AutoField(primary_key=True)
    typeuser=models.IntegerField()
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250) """


class Freelancer(models.Model):
    idfreelancer = models.OneToOneField(User, on_delete=models.CASCADE)
    idcard = models.IntegerField()
    name=models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthday = models.DateField()
    idcountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    idcity = models.ManyToManyField(City)
    idneighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    length = models.FloatField(default=0)
    address = models.CharField(max_length=300)
    description = models.TextField(default="")
    imageprofile =models.ImageField(upload_to='freelancer/images/', default= 'freelancer/images/default-avatar-profile.jpg')
    imagejobs =models.ImageField(upload_to='freelancer/images/', default="freelancer/images/default-image-5-1.jpg")
    idservices = models.ForeignKey(Service, on_delete=models.CASCADE)

class Customer(models.Model):
    idcustomer = models.ForeignKey(User, on_delete=models.CASCADE)
    idcard = models.IntegerField()
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthday = models.DateField()
    imageprofile =models.ImageField(upload_to='customer/images/')
    idcountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    idcity = models.ForeignKey(City, on_delete=models.CASCADE)
    idneighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)

class Request(models.Model):
    idrequest = models.AutoField(primary_key=True)
    idcustomer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='1')
    idfreelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    requestday = models.DateField()
    requesttime = models.TimeField()
    address = models.CharField(max_length=300)
    phone= models.IntegerField()
    state = models.CharField(max_length=100, default="Pendiente")

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    idfreelancer = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name




