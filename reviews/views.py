from django.shortcuts import render

from reviews.models import Review


def one_hotel(request, id_hotels: int):
    reviews = Review.objects.filter(hotel_id=id_hotels)
    review_dict = {'review_for_hotel': reviews
                   }
    return render(request, 'reviews/all_reviews_for_hotels.html', review_dict)