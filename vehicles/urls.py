from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_vehicles, name='vehicles'),
    path('<vehicle_id>', views.vehicle_detail, name='vehicle_detail'),  
]