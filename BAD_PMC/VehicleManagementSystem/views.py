from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.templatetags.static import static
from .forms import UserRegistrationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if user.role == "driver":
                # return redirect("driver_dashboard")
            # elif user.role == "management":
                # return redirect("management_dashboard")
            # else:
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "VehicleManagementSystem/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
            print(form.errors)
    else:
        form = UserRegistrationForm()  # Create a blank form when GET request

    return render(request, "VehicleManagementSystem/register.html", {"form": form})


@login_required
def driver_dashboard(request):
    return render(request, "VehicleManagementSystem/driver_dashboard.html")

@login_required
def management_dashboard(request):
    return render(request, "VehicleManagementSystem/management_dashboard.html")

@login_required
def dashboard(request):
    sample_vehicles = [
        {
            "plate_number": "ABC123",
            "status": "Operational",
            # "image": "https://placehold.co/300x300?text=Truck+1",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "January 8, 2021",
            "damages": ["Minor scratch on bumper", "Replaced headlights"],
        },
        {
            "plate_number": "XYZ789",
            "status": "In Repair",
            # "image": "https://placehold.co/300x300?text=Truck+2",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "February 15, 2021",
            "damages": ["Engine overheating", "Transmission issues"],
        },
        {
            "plate_number": "LMN456",
            "status": "Unavailable",
            # "image": "https://placehold.co/300x300?text=Truck+3",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "March 10, 2021",
            "damages": ["Broken axle", "Flat tire"],
        },
        {
            "plate_number": "DEF789",
            "status": "Operational",
            # "image": "https://placehold.co/300x300?text=Truck+4",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "April 20, 2021",
            "damages": ["Oil leak", "Brake pad replacement"],
        },
        {
            "plate_number": "GHI234",
            "status": "In Repair",
            # "image": "https://placehold.co/300x300?text=Truck+5",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "May 5, 2021",
            "damages": ["Electrical failure", "Fuel pump replacement"],
        },
        {
            "plate_number": "JKL567",
            "status": "Unavailable",
            # "image": "https://placehold.co/300x300?text=Truck+6",
            "image": static("myapp/images/300x300.svg"),
            "last_maintenance": "June 25, 2021",
            "damages": ["Severe engine damage", "Total transmission failure"],
        },
    ]

    return render(request, "VehicleManagementSystem/dashboard.html", {"sample_vehicles": sample_vehicles})
