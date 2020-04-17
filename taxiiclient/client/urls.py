from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('login', TemplateView.as_view(template_name='index.html')),
    path('dashboard', TemplateView.as_view(template_name='dashindex.html')),
    
    
]
    

