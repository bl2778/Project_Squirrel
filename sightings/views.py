from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm


def index(request):
    return render(request, 'sightings/index.html', {})


def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/list.html', context)


def stats(request):
    squirrels = Squirrel.objects
    squnumber = squirrels.count()
    amnumber = squirrels.filter(Shift='AM').count()
    pmnumber = squirrels.filter(Shift='PM').count()
    adultnumber = squirrels.filter(Age='Adult').count()
    junumber = squirrels.filter(Age='Juvenile').count()
    graynumber = squirrels.filter(Primary_fur_color='Gray').count()
    cinnumber = squirrels.filter(Primary_fur_color='Cinnamon').count()
    blacknumber = squirrels.filter(Primary_fur_color='Black').count()
    groundnumber = squirrels.filter(Location='Ground Plane').count()
    abgrnumber = squirrels.filter(Location='Above Ground').count()
    runnumber = squirrels.filter(Running=True).count()

    context = {'squnumber': squnumber, 'amnumber': amnumber, 'pmnumber': pmnumber,
               'adultnumber': adultnumber, 'junumber': junumber,'graynumber': graynumber,'cinnumber':cinnumber,
               'blacknumber':blacknumber, 'groundnumber':groundnumber, 'abgrnumber':abgrnumber, 'runnumber':runnumber}
    return render(request, 'sightings/stats.html', context)


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
