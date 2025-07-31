# main_app/views.py

from django.shortcuts import render
from .models import Cat
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function


def home(request):
    return render(request, 'index.html')

# Define the about view function


def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # Fetch all cats from the database
    cats = Cat.objects.all()
    # Render the 'cats/index.html' template with the list of cats
    return render(request, 'cats/index.html', {'cats': cats})

# def cats(request):
#     # You can render a template or return a simple response
#     return render(request, 'cats.html')

    # You can render a template or return a simple response
    return render(request, 'cats.html')
