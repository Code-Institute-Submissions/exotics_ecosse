from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def all_vehicles(request):
    """view to show all vehicles plus sorting and search queries"""

    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
    }

    return render(request, 'vehicles/vehicles.html', context)