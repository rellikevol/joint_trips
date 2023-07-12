from django.urls import path
from trips import views


urlpatterns = [
    path('search/', views.trips_search, name='trips-search'),
    path('add_trip/', views.add_trip, name='add-trip')
]