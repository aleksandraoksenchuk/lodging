from django.shortcuts import render


from places.models import Hotel, Room
from cities.models import City


def all_hotels_in_the_city(request, id_city: int):
    hotels_list = Hotel.objects.filter(city_id=id_city)
    one_city = City.objects.get(id=id_city)
    hotels_dict = {'hotels': hotels_list,
                   'city': one_city}
    return render(request, 'places/hotels/all_hotels_in_the_city.html', hotels_dict)


def one_hotel(request, id_city: int, id_hotels: int):
    hotel = Hotel.objects.get(id=id_hotels)
    rooms = Room.objects.filter(hotel_id=id_hotels)
    one_city = City.objects.get(id=id_city)
    rooms_dict = {'hotel': hotel,
                  'rooms_in_hotel': rooms,
                  'city': one_city}
    return render(request, 'places/hotels/one_hotel_in_the_city.html', rooms_dict)



