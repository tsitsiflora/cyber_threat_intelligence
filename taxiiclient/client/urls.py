from django.urls import path, include
from .views import *


urlpatterns = [
    path('login', login_view, name='Login'),
    path('dashboard', dashboard_view, name='Dashboard'),
    path('icon', icon_view, name='IconMaterial'),
    path('error404', error404_view, name='Error404'),
    path('profile', profile_view, name='Profile'),
    path('table', table_view, name='Table'),
    path('starterkit', starter_view, name='StarterKit'),
    
]
    

