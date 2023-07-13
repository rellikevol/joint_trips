from django.shortcuts import render


# Create your views here.

def register(request):
    return render(request, 'users/register_page.html')

def enter(request):
    return render(request, 'users/enter_page.html')
