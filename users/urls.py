from django.urls import path, include
from users import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register_done, name='register-done'),
    path('not_register/', views.not_register, name='not-register'),
    path('edit_profile/', views.edit_profile, name='edit-profile')
]
