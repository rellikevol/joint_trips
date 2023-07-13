from django.urls import path
from users import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('enter/', views.enter, name='enter')
]