from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    idcountry = models.AutoField(primary_key=True)
    namecounty= models.CharField(max_length=250)
 
class City(models.Model):
    idcity = models.AutoField(primary_key=True)
    namecity= models.CharField(max_length=250)
    idcountry = models.ForeignKey(Country, on_delete=models.CASCADE)

class Neighborhood(models.Model):
    idneighborhood = models.AutoField(primary_key=True)
    nameneighborhood= models.CharField(max_length=250)
    idcity = models.ForeignKey(City, on_delete=models.CASCADE)

class Services(models.Model):
    idservices= models.AutoField(primary_key=True)
    name= models.CharField(max_length=250)

class User(models.Model):
    iduser= models.AutoField(primary_key=True)
    typeuser=models.IntegerField()
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
 
class Freelancer(models.Model):
    idfreelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    idcard = models.IntegerField()
    name=models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthday = models.DateField()
    idcountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    idcity = models.ForeignKey(City, on_delete=models.CASCADE)
    idneighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    imageprofile =models.ImageField(upload_to='freelancer/images/')
    imagejobs =models.ImageField(upload_to='freelancer/images/')
    idservices = models.ForeignKey(Services, on_delete=models.CASCADE)

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

class Schedule(models.Model):
    idschedule= models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    date = models.DateField()
    startime = models.TimeField ()
    endtime = models.TimeField ()
    state = models.IntegerField()

class Request(models.Model):
    idrequest = models.AutoField(primary_key=True)
    idcustomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    idfreelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    idschedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    registerday = models.DateField()
    state = models.IntegerField()





    



