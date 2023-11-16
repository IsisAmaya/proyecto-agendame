from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name="search"),
    path('solicitud/<int:idfreelancer>', views.solicitud, name="solicitud"),
    path('register/step1_/', views.registration_step1_, name='registration_step1_'),
    path('register/step2_/', views.registration_step2_, name='registration_step2_'),
    path('register/complete/', views.registration_complete_, name="registration_complete_"),
    path('login_/', views.login_customer_, name="login"),
    path('logout/', views.logout_customer, name="logout"),
    path('profile_/', views.profile_, name="profile_"),
    path('profile/edit/', views.edit_profile_, name="edit_profile_"),
    path('profile/update/', views.update_profile_, name="update_profile_"),
    ##path('<int:freelancer_id>', views.detail, name='detail'),
]