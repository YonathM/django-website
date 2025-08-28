from django.contrib import admin
from django.urls import path, include
from . import views

# Customize Django admin headers
admin.site.site_header = "DEBRE TABOR POLYTECHNIC COLLEGE"
admin.site.site_title = "Admin Panel"
#admin.site.index_title = "Welcome to the Dashboard"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]

