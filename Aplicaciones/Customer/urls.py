from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name="search"),
    path('solicitud/<int:idfreelancer>', views.solicitud, name="solicitud"),
    ##path('<int:freelancer_id>', views.detail, name='detail'),
]