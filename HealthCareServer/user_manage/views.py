from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_page(request): 
      
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()             
    
    context = {'form': form}
    return render(request, "accounts/register.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return redirect('dashboard')

    return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")
