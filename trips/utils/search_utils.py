from trips.models import Trip
from datetime import datetime

def search_in_trips(context):
    all_results = Trip.objects.filter(in_process=True,
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
        return {'is_success': False,'result': all_results, 'date_correct': False}
