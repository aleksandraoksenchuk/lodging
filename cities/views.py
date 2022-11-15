from django.shortcuts import render

from cities.models import City


def all_cities(request):
    city_list = City.objects.all()
    cities_dict = {'cities': city_list}
    return render(request, 'cities/all_cities.html', cities_dict)



