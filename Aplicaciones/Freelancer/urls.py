from django.urls import path
from . import views


urlpatterns = [
    path('register/step1/', views.registration_step1, name='registration_step1'),
    path('register/step2/', views.registration_step2, name='registration_step2'),
    path('register/complete/', views.registration_complete, name="registration_complete"),
    path('login/', views.login_freelancer, name="login"),
    path('logout/', views.logout_freelancer, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/update/', views.update_profile, name="update_profile"),
    path('calendarioFreelancer/', views.calendar, name="calendar"),
    path('<int:freelancer_id>', views.detail, name='detail'),
    path('filter/<str:categoria>/', views.filter_category,name='filter_services'),
]
