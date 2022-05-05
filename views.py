from django.shortcuts import render
from .models import *


def index(request):
    desserts = Dessert.objects.all()
    return render(request, 'cafe/index.html', {'desserts': desserts})

def about(request):
    return render(request, 'cafe/about.html')