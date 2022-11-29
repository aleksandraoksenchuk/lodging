from django.urls import path
from .views import *


urlpatterns = [
    path('', all_hotels_in_the_city),
    path('<int:id_hotels>', one_hotel),
]
