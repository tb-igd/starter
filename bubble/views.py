from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class Bubble(View):

    def get(self, request):
        return HttpResponse('ok', status=200)
