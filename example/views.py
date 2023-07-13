from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'example/main_page.html')

def how_it_works(request):
    return render(request, 'example/how_it_works_page.html')



