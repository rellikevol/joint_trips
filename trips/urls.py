from django.urls import path
from trips import views


urlpatterns = [
    path('search/', views.trips_search, name='trips-search'),
    path('add_trip/', views.add_trip, name='add-trip'),
    path('<int:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('my_trips/', views.my_trips, name='my-trips'),
    path('book/<int:pk>', views.book_trip, name='book-trip'),
    path('cancel/<int:pk>', views.cancel_book, name='cancel-trip'),
    path('delete/<int:pk>', views.delete_trip, name='delete-trip'),
    path('start/<int:pk>', views.start_trip, name='start-trip'),
    path('end/<int:pk>', views.end_trip, name='end-trip')
]