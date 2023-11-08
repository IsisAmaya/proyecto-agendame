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
    # path('calendarioFreelancer/<int:idfreelancer>', views.uploadschedule, name="uploadschedule"),
    # path('calendarioFreelancer/<int:idschedule>/delete', views.deleteSchedule, name="deleteSchedule"),
    path('<int:freelancer_id>', views.detail, name='detail'),
    path('filter/<str:categoria>/', views.filter_category,name='filter_services'),
    path('profile/analitics/', views.analitic, name="analitic"),
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/all_events/', views.all_events, name='all_events'),
    path('calendar/add_event/', views.add_event, name='add_event'),
    path('calendar/update/', views.update, name='update'),
    path('calendar/remove/', views.remove, name='remove'),
    path('request/', views.request, name='request'),
    path('request/<int:idrequest>/update', views.updateRequest, name="updateRequest"),
]
