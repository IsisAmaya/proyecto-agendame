from django.contrib import admin
from .models import Freelancer
from .models import Country
from .models import City
from .models import Neighborhood
from .models import Services
from .models import User
from .models import Customer
from .models import Request
from .models import Schedule

# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Services)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Request)
admin.site.register(Schedule)
