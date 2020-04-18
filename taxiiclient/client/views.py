from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
  
# Create your views here. 
def login_view(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return render(request, "dashindex.html")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'index.html', {})
    
def dashboard_view(request):
    return render(request, 'dashindex.html')

def icon_view(request):
    return render(request, 'icon-material.html')

def error404_view(request):
    return render(request, 'error-404.html')

def profile_view(request):
    return render(request, 'pages-profile.html')

def table_view(request):
    return render(request, 'table-basic.html')

def starter_view(request):
    return render(request, 'starter-kit.html')