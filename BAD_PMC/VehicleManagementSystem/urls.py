from django.urls import path
from .views import login_view, logout_view, register_view, driver_dashboard, management_dashboard, dashboard

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("driver/dashboard/", driver_dashboard, name="driver_dashboard"),
    path("management/dashboard/", management_dashboard, name="management_dashboard"),
    path("dashboard/", dashboard, name="dashboard"),
]
