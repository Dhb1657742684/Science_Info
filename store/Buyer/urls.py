from django.urls import path, re_path
from Buyer.views import *

urlpatterns = [
    path('index/', index),
    path('base/', index),
    path('register/', register),
    path('login/', login),
    # path('Buyer', include('Buyer.urls')),
]
