from django.shortcuts import render, redirect

from places.forms import BookingForm
from places.models import Hotel, Room, Booking
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


def booking_room(request, id_city: int, id_hotels: int):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking', id_city, id_hotels)
    else:
        form = BookingForm()
        rooms = Room.objects.all()
        one_booking_room = Booking.objects.all()
    # first_date = True
    # booking = Booking.objects.get(id=first_date)
    # if datetime.now() > booking:
    #     first_date = False
    # return render(request, template, {'is_alive': is_alive})
        booking_dict = {'rooms_in_hotel': rooms,
                        'one_city': id_city,
                        'hotel': id_hotels,
                        'booking_room': one_booking_room,
                        'form': form}
        return render(request, 'places/booking/booking.html', booking_dict)




