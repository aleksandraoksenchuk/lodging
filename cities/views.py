from django.http import HttpResponse
from django.shortcuts import render

from cities.models import City


def all_cities(request):
    city_list = City.objects.all()
    for city in city_list:
        print(city.name)
    cities_dict = {'cities': city_list}
    return render(request, 'cities/all_cities.html', cities_dict)


def get_city(request, id_city: int):
    name = City.objects.get(pk=id_city)
    return HttpResponse(name)
