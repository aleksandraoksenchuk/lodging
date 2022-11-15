from django.http import HttpResponse
from django.shortcuts import render


from places.models import Hotel


def all_hotels_in_the_city(request):
    hotels_list = Hotel.objects.filter(pk='City')
    hotels_dict = {'hotels': hotels_list}
    return render(request, 'places/all_hotels_in_the_city.html', hotels_dict)


def one_hotel(request, id_hotels: int):
    name = City.objects.get(pk=title)
    return HttpResponse(name)



# from .models import Cat
#
# from accounts.forms import LoginForm
#
#
# def index(request):
#     page_number = request.GET.get('page')
#     baby_age = request.GET.get('baby_age')
#     senior_age = request.GET.get('senior_age')
#     gender_male = request.GET.get('gender_male')
#     gender_female = request.GET.get('gender_female')
#
#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1
#
#     filters = Q()
#     page_extra = []
#
#     filters_age = Q()
#     if baby_age:
#         filters |= Q(age="Baby")
#         filters_age |= Q(age="Baby")
#         page_extra.append("baby_age=true")
#     if senior_age:
#         filters |= Q(age="Senior")
#         filters_age |= Q(age="Senior")
#         page_extra.append("senior_age=true")
#
#     filters_gender = Q()
#     if gender_male:
#         filters_gender |= Q(gender="Male")
#         page_extra.append("gender_male=true")
#     if gender_female:
#         filters_gender |= Q(gender="Female")
#         page_extra.append("gender_male=true")
#
#     filters = filters_age & filters_gender
#
#     if page_extra:
#         page_extra = "&" + "&".join(page_extra)
#     else:
# @@ -32,6 +47,8 @@ def index(request):
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'form': LoginForm(),
#         "user": request.user,
#         'num_visits': num_visits,
#         'page_obj': page_obj,
#         "baby_age": baby_age,
