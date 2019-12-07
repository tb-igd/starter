from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'caterpy'
urlpatterns = [
    path('', Bubble.as_view(), name='bubble'),
]
