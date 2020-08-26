from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Vehicle, Category
from .forms import VehicleForm

# Create your views here.

def all_vehicles(request):
    """ A view to show all cars, including sorting and search queries """

    vehicles = Vehicle.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                vehicles = vehicles.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            vehicles = vehicles.order_by(sortkey)

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

    current_sorting =f'{sort}_{direction}'

    context = {
        'vehicles': vehicles,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_id):
    """ A view to show individual cars details """

    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    context = {
        'vehicle': vehicle,
    }

    return render(request, 'vehicles/vehicle_detail.html', context)


def add_vehicle(request):
    """ Add a vehicle """
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save()
            messages.success(request, 'Successfully added vehicle!')
            return redirect(reverse('vehicle_detail', args=[vehicle.id]))
        else:
            messages.error(request, 'Failed to add vehicle. Please ensure the form is valid.')
    else:           
        form = VehicleForm()
        
    template = 'vehicles/add_vehicle.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_vehicle(request, vehicle_id):
    """edit a vehicle """
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated vehicle')
            return redirect(reverse('vehicle_detail', args=[vehicle.id]))
        else:
            messages.error(request, 'Failed to update vehicle. Please ensure form is valid')
    else:
        form = VehicleForm(instance=vehicle)
        messages.info(request, f'You are editing {vehicle.name}')

    template = 'vehicles/edit_vehicle.html'
    context = {
        'form': form,
        'vehicle': vehicle,
    }

    return render(request, template, context)

def delete_vehicle(request, vehicle_id):
    """delete vehicle"""
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle.delete()
    messages.success(request, 'Vehicle deleted!')
    return redirect(reverse('vehicles'))


