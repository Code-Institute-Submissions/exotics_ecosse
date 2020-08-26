from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_vehicles, name='vehicles'),
    path('<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('add/', views.add_vehicle, name='add_vehicle'),  
]