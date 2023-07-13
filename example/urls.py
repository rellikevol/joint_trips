from django.urls import path
from example import views


urlpatterns = [
    path('', views.index, name='index-page'),
    path('how_it_works/', views.how_it_works, name='how-it-works')
]