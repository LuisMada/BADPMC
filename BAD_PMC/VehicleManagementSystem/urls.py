from django.urls import path
from .views import login_view, logout_view, register_view, dashboard, create_report # driver_dashboard, management_dashboard,

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    # path("driver/dashboard/", driver_dashboard, name="driver_dashboard"),
    # path("management/dashboard/", management_dashboard, name="management_dashboard"),
    path("dashboard/", dashboard, name="dashboard"),
    # create report
    path("reports/create/", create_report, name="create_report"),
]