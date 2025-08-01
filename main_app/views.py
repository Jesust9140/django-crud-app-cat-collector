# main_app/views.py

from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Toy list CBV
from django.views.generic import ListView
from .models import Cat, Toy
# Toy create CBV


class ToyList(ListView):
    model = Toy
    template_name = 'main_app/toy_list.html'
    context_object_name = 'toys'


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


# Import HttpResponse to send text-based responses

# Register your models here.

# Define the home view function


def home(request):
    return render(request, 'index.html')

# Define the about view function


def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})
# Add view to handle feeding form submission


def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
