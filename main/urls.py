from django.urls import path
from . import views

urlpatterns=[
    path('', views.display_homepage, name='display_homepage'),
    path('services/', views.view_services, name='services'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('financial/', views.financial, name='financial'),

    
]