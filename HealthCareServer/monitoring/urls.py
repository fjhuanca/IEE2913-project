from django.urls import path
from .views import dashboard_page, chart_test

urlpatterns = [
    path('dashboard/', dashboard_page, name="dashboard"),
    path('temp_test/', chart_test, name="chart_test")
]