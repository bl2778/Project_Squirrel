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
