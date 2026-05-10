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
    path('missionandvision/', views.missionandvision, name='missionandvision'),
    path('deanmessage/', views.deanmessage, name='deanmessage'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news_list, name='news_list'),          # News listing page
     # News detail page
    path('news/<int:news_id>/', views.selectedNews, name='news_detail'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
   path("department/<int:pk>/", views.department_detail, name="department"),
   path("tuitionfees/", views.tuitionfee_list, name="tuitionfee"),  
   path('send-contact-email/', views.send_contact_email, name='send_contact_email'),  # handles submission
    path('digital-libraries/', views.digital_library_list, name='digital_library_list'),
    path('digital-libraries/<int:dig_id>/', views.digital_library_detail, name='digital_library_detail'),
    path('production-units/', views.production_unit_list, name='production_unit_list'),
    path('production-units/<int:unit_id>/', views.production_unit_detail, name='production_unit_detail'),   
    path('tenders/', views.tender_list, name='tender_list'),
    path('tenders/<int:tender_id>/', views.tender_detail, name='tender_detail'),   
]

