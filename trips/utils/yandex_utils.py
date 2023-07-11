from yandex_geocoder import Client, exceptions
import os
from dotenv import load_dotenv
from core.settings import BASE_DIR
from decimal import Decimal
from yandex_geocoder.exceptions import NothingFound

load_dotenv(os.path.join(BASE_DIR, '.env'))
ya_api_key = os.environ.get('API_YANDEX_GEO')

locality_names = ['locality', 'area', 'province', 'district', 'house', 'country']


class ClientTwo(Client):
    def get_adress_description(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        got = self._request(f"{longitude},{latitude}")
        data = got["GeoObjectCollection"]["featureMember"]
        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]['Address']['Components']


def geocode_to_str(code):
    return {'longitude': str(code[0]), 'latitude': str(code[1])}


def str_to_geocode(code):
    return (Decimal(code['longitude']), Decimal(code['latitude']))


def get_geocode(address):
    client1 = ClientTwo(ya_api_key)
    try:
        code = client1.coordinates(address)
    except exceptions.YandexGeocoderException:
        return {'status': False, 'exist': False, 'other': True}
    except Exception:
        return {'status': False, 'exist': True, 'other': False}
    else:
        return {'status': True, 'exist': True, 'other': True, 'code': geocode_to_str(code)}


def get_address(code):
    client1 = ClientTwo(ya_api_key)
    try:
        address = client1.address(code)
    except exceptions.YandexGeocoderException:
        return {'status': False, 'exist': False, 'other': True}
    except Exception:
        return {'status': False, 'exist': True, 'other': False}
    else:
        return {'status': True, 'exist': True, 'other': True, 'address': address}


def get_full_address_description(code):
    client1 = ClientTwo(ya_api_key)
    try:
        address_description = client1.get_adress_description(code[0], code[1])
    except exceptions.YandexGeocoderException:
        return {'status': False, 'exist': False, 'other': True}
    except Exception:
        return {'status': False, 'exist': True, 'other': False}
    else:
        return {'status': True, 'exist': True, 'other': True, 'address': address_description}


def get_locality_name(code):
    description = get_full_address_description(code)
    if description['status']:
        for i in locality_names:
            for x in description['address']:
                if x['kind'] == i:
                    description['address'] = x['name']
                    return description
        adr = get_address(code)
        if adr['status']:
            description['address'] = adr['address']
            return description
        else:
            return adr
    else:
        return description


