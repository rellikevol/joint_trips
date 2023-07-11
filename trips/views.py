from django.shortcuts import render, redirect
from trips.models import Trip
from trips.utils.yandex_utils import get_geocode, get_locality_name, str_to_geocode
from trips.utils.search_utils import search_in_trips
from django.views import generic


# Create your views here.


def trips_search(request):
    if request.method == 'POST':

        context = {'suggest1': request.POST.get('suggest1'),
                   'suggest2': request.POST.get('suggest2'),
                   'date': request.POST.get('date'),
                   'space': request.POST.get('space'),
                   'is_lucky': True,
                   'error': 'No'}

        geo_from = get_geocode(request.POST.get('suggest1'))
        geo_to = get_geocode(request.POST.get('suggest2'))

        if geo_from['status'] and geo_to['status']:
            locality_from = get_locality_name(str_to_geocode(geo_from['code']))
            locality_to = get_locality_name(str_to_geocode(geo_to['code']))

            if locality_from['status'] and locality_to['status']:
                context['locality_from'] = locality_from['address']
                context['locality_to'] = locality_to['address']
                result = search_in_trips(context)

                if result['is_success']:
                    context['result'] = result['result']
                    context['date_correct'] = result['date_correct']

                context['is_search_had_result'] = result['is_success']
                return render(request, 'trips/search.html', context=context)
            else:
                context['is_lucky'] = False

                if not locality_from['exist'] and locality_to['exist']:
                    context['error'] = 'Такого адреса нет...'

                if not locality_from['other'] and locality_to['other']:
                    context['error'] = 'Что-то пошло не так...'

                return render(request, 'trips/search.html', context=context)
        else:
            context['is_lucky'] = False

            if not geo_from['exist'] or not geo_to['exist']:
                context['error'] = 'Такого адреса нет...'

            if not geo_from['other'] or not geo_to['other']:
                context['error'] = 'Что-то пошло не так...'

            return render(request, 'trips/search.html', context=context)
    else:
        return render(request, 'trips/search.html')
