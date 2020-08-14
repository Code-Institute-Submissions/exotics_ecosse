from django.shortcuts import render, get_object_or_404
from . models import Vehicle

# Create your views here.

def all_vehicles(request):
    """ A view to show all cars, including sorting and search queries """

    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
    }

    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_id):
    """ A view to show individual cars details """

    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    context = {
        'vehicle': vehicle,
    }

    return render(request, 'vehicles/vehicle_detail.html', context)