from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Vehicle, Category

# Create your views here.

def all_vehicles(request):
    """ A view to show all cars, including sorting and search queries """

    vehicles = Vehicle.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            vehicles = vehicles.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('vehicles'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            vehicles = vehicles.filter(queries)

    context = {
        'vehicles': vehicles,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_id):
    """ A view to show individual cars details """

    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    context = {
        'vehicle': vehicle,
    }

    return render(request, 'vehicles/vehicle_detail.html', context)