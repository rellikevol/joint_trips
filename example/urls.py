from django.urls import path
from example import views


urlpatterns = [
    path('', views.index, name='index-page'),
    path('how_it_works/', views.how_it_works, name='how-it-works'),
    path('about_us/', views.about_us, name='about-us'),
    path('contacts/', views.contacts, name='contacts'),
    path('terms_of_use/', views.terms_of_use, name='terms-of-use'),
    path('privacy_policy/', views.privacy_policy, name='privacy-policy')
]