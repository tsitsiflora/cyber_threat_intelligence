from django.urls import path, include
from .views import *


urlpatterns = [
    path('login', login_view, name='Login'),
    path('dashboard', dashboard_view, name='Dashboard'),
    path('profile', profile_view, name='Profile'),
    path('table', table_view, name='Table'),
    path('new', newioc_view, name='Post_new'),
    
]
    

