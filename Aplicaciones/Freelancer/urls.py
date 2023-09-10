from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up, name="sign_up"),
    path('calendarioFreelancer/', views.calendar, name="calendar"),
    path('<int:freelancer_id>', views.detail, name='detail'),
    path('filter/<str:categoria>/', views.filter_category,name='filter_services'),
]
