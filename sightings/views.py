from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def map(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/map.html', {'squirrels':squirrels})


def edit_squirrel(request, Unique_squirrel_id):
    squirrel = Squirrel.objects.get(Unique_squirrel_id=Unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/list')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:list')

    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/add.html', context)
# Create your views here.
