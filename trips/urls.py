from django.urls import path
from trips import views


urlpatterns = [
    path('search/', views.trips_search, name='trips-search'),
    path('add_trip/', views.add_trip, name='add-trip'),
    path('<int:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('my_trips/', views.my_trips, name='my-trips'),
    path('book/<int:pk>', views.book_trip, name='book-trip'),
    path('cancel/<int:pk>', views.cancel_book, name='cancel-trip')
]