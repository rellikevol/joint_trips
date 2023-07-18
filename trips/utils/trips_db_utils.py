from trips.models import Trip
from datetime import datetime
from trips.utils.yandex_utils import get_locality_name, str_to_geocode


def search_in_trips(context):
    all_results = Trip.objects.filter(is_active=True,
                                      in_process=False,
                                      is_finished=False,
                                      locale_from__icontains=context['locality_from'],
                                      locale_to__icontains=context['locality_to'],
                                      empty_spaces__gte=context['space'])
    search_day = datetime.strptime(context['date'], '%Y-%m-%d')

    if len(all_results) > 0:
        today_results = all_results.filter(date=search_day)
        if len(today_results) > 0:
            return {'is_success': True, 'result': today_results, 'date_correct': True}
        else:
            any_day_results = all_results.filter(date__gte=search_day)
            if len(any_day_results) > 0:
                return {'is_success': True, 'result': any_day_results, 'date_correct': False}
            else:
                return {'is_success': False, 'result': any_day_results, 'date_correct': False}
    else:
        return {'is_success': False, 'result': all_results, 'date_correct': False}


def append_trip(context):

    locale_from = get_locality_name(str_to_geocode(context['geo_from_data']))
    locale_to = get_locality_name(str_to_geocode(context['geo_to_data']))

    if not locale_from['status'] or not locale_to['status']:
        return {'status': False, 'pk': -1}

    if not context['form'].is_valid():
        return {'status': False, 'pk': -1}

    trip = Trip.objects.create(locale_from=locale_from['address'],
                               point_from=context['suggest1'],
                               longitude_from=context['geo_from_data']['longitude'],
                               latitude_from=context['geo_from_data']['latitude'],
                               locale_to=locale_to['address'],
                               point_to=context['suggest2'],
                               longitude_to=context['geo_to_data']['longitude'],
                               latitude_to=context['geo_to_data']['latitude'],
                               date=context['date'],
                               time=context['time'],
                               spaces=context['space'],
                               empty_spaces=context['space'],
                               is_active=True,
                               owner=context['owner'].user_profile,
                               can_smoke=context['form'].cleaned_data['can_smoke'],
                               with_animals=context['form'].cleaned_data['with_animals']
                               )

    trip.save()

    return {'status': True, 'pk': trip.pk}