from django.urls import path
from .views import *


urlpatterns = [
    path('', review, name='reviews'),
]
