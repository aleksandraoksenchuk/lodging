from django.http import HttpResponse
from django.shortcuts import render


from places.models import Hotel
from cities.models import City


def all_hotels_in_the_city(request, id_city: int):
    hotels_list = Hotel.objects.filter(city_id=id_city)
    one_city = City.objects.get(id=id_city)
    hotels_dict = {'hotels': hotels_list,
                   'city': one_city}
    return render(request, 'places/hotels/all_hotels_in_the_city.html', hotels_dict)


# def one_hotel(request, id_hotels: int):
#     name = City.objects.get(pk=title)
#     return HttpResponse(name)



