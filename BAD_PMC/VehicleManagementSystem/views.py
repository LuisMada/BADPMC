from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == "driver":
                return redirect("driver_dashboard")
            elif user.role == "management":
                return redirect("management_dashboard")
            else:
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
        form = UserRegistrationForm()
    return render(request, "VehicleManagementSystem/register.html", {"form": form})

@login_required
def driver_dashboard(request):
    return render(request, "VehicleManagementSystem/driver_dashboard.html")

@login_required
def management_dashboard(request):
    return render(request, "VehicleManagementSystem/management_dashboard.html")

@login_required
def dashboard(request):
    return render(request, "VehicleManagementSystem/dashboard.html")
