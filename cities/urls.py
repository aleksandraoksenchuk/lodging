from django.urls import path, include
from .views import *


urlpatterns = [
    path('', all_cities),
]
