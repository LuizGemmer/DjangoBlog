from django.shortcuts import render
from django.views import generic

# Create your views here.
#class HomeView(generic.ListView):
#    template_name='blogApp/home.html'

def home(request):
    return render(request, template_name='blogApp/home.html')