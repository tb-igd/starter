from django.shortcuts import render
from django.views import View

# Create your views here.

class Bubble(View):

    def get(self, request):
        return render(request, 'bubble/noises.html')
    
