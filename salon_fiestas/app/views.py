from django.shortcuts import render, redirect, get_object_or_404
from .models import RESERVACION, SHOW

# Create your views here.


def inicio(request):
    return render(request, 'index.html')