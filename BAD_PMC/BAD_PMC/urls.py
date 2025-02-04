
from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VehicleManagementSystem.urls')),  # Include URLs from your app
]
