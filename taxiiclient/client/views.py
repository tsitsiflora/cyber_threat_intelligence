from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from taxii2client.v20 import Server
from .forms import IndicatorForm
from stix2 import Indicator
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

def profile_view(request):
    return render(request, 'pages-profile.html')

def table_view(request):
    server = Server('https://limo.anomali.com/api/v1/taxii2/taxii/', user='guest', password='guest')
    api_root = server.api_roots[0]
    collection = api_root.collections[0]
    title = collection.title()
    objects = collection.get_objects()
    #print(collection.title)
    #print(objects)

    return render(request, 'table-basic.html',title, objects)

def newioc_view(request):
    if request.method == 'POST':
        form = IndicatorForm(request.POST)
        if form.is_valid():
            newioc = form.save(commit=False)
            indicator = Indicator(name=form.name, labels=form.labels, pattern=form.pattern)
            return redirect('dashindex.html')
    else:
        form = IndicatorForm
    return render(request, 'newioc.html', {'form': form})
