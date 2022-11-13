from django.http import HttpResponse

from cities.models import City


def all_cities(request):
    cities = City.objects.all()
    return HttpResponse(cities)


def get_city(request, id_city: int):
    name = City.objects.get(pk=id_city)
    return HttpResponse(name)
