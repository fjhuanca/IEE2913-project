from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template

# Create your views here.
def index_view(request):
    return render(request, "index.html")

