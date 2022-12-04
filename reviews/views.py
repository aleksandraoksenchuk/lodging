from django.shortcuts import render, redirect

from cities.models import City
from places.models import Hotel
from .forms import ReviewsForm
from .models import Review


def review(request, id_city: int, id_hotels: int):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews', id_city, id_hotels)

    else:
        form = ReviewsForm()
        hotel = Hotel.objects.get(id=id_hotels)
        reviews = Review.objects.filter(hotel_id=id_hotels)
        one_city = City.objects.get(id=id_city)
        review_dict = {
            'review_for_hotel': reviews,
            'hotel': hotel,
            'city': one_city,
            'form': form
        }
        return render(request, 'reviews/all_reviews_for_hotels.html', review_dict)


