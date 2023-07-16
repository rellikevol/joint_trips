from django.shortcuts import render, redirect
from trips.models import Trip
from trips.utils.yandex_utils import get_geocode, get_locality_name, str_to_geocode
from trips.utils.trips_db_utils import search_in_trips, append_trip
from django.views import generic
from django.urls import reverse_lazy


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
                return render(request, 'trips/search_page.html', context=context)
            else:
                context['is_lucky'] = False

                if not locality_from['exist'] and locality_to['exist']:
                    context['error'] = 'Такого адреса нет...'

                if not locality_from['other'] and locality_to['other']:
                    context['error'] = 'Что-то пошло не так...'

                return render(request, 'trips/search_page.html', context=context)
        else:
            context['is_lucky'] = False

            if not geo_from['exist'] or not geo_to['exist']:
                context['error'] = 'Такого адреса нет...'

            if not geo_from['other'] or not geo_to['other']:
                context['error'] = 'Что-то пошло не так...'

            return render(request, 'trips/search_page.html', context=context)
    else:
        return render(request, 'trips/search_page.html')


def add_trip(request):
    if not request.user.is_authenticated:
        return redirect('not-register')
    if request.method == 'POST':

        context = {'suggest1': request.POST.get('suggest1'),
                   'suggest2': request.POST.get('suggest2'),
                   'date': request.POST.get('date'),
                   'time': request.POST.get('time'),
                   'space': request.POST.get('seats'),
                   'is_lucky': True}

        geo_from = get_geocode(request.POST.get('suggest1'))
        geo_to = get_geocode(request.POST.get('suggest2'))

        if geo_from['status'] and geo_to['status']:
            context['geo_from'] = True
            context['geo_to'] = True
            context['geo_from_data'] = geo_from['code']
            context['geo_to_data'] = geo_to['code']

            result = append_trip(context)

            if result['status']:
                return redirect('trip-detail', pk=result['pk'])
            else:
                context['is_lucky'] = False
                return render(request, 'trips/add_trip.html', context=context)
        else:
            if not geo_from['status']:
                context['geo_from'] = False
            else:
                context['geo_from'] = True

            if not geo_to['status']:
                context['geo_to'] = False
            else:
                context['geo_to'] = True

        return render(request, 'trips/add_trip.html', context=context)
    else:
        return render(request, 'trips/add_trip.html')


class TripDetailView(generic.DetailView):
    model = Trip
    context_object_name = "trip"
    template_name = "trips/trip_detail_page.html"
    lookup_field = 'pk'
