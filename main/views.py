from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def display_homepage(request):
    """
    View function to dispaly the homepage
    """
    project_details=Project.objects.all()
    
    return render(request, 'index.html', {'project_details':project_details})


def view_services(request):
    """
    """
    return render(request, 'services.html')

def contact_us(request):
    """
    """
    return render(request, 'contact.html')

def about_us(request):
    """
    """
    return render(request, 'about.html')

def financial(request):
    """
    """
    return render(request, 'financial.html')



    