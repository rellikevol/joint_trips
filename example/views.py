from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'example/main_page.html')


def how_it_works(request):
    return render(request, 'example/how_it_works_page.html')


def about_us(request):
    return render(request, 'example/about_us_page.html')


def contacts(request):
    return render(request, 'example/contacts_page.html')


def terms_of_use(request):
    return render(request, 'example/terms_of_use.html')


def privacy_policy(request):
    return render(request, 'example/privacy_policy.html')
