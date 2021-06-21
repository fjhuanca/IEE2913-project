from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def dashboard_page(request):
    return render(request, "dashboard.html")

def chart_test(request):
    return render(request, "chart_test.html")