from django.urls import path
from example import views


urlpatterns = [
    path('', views.index, name='index-page')
]