from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News, Department, Statistic, Tender, Testimonial, Vacancy, TuitionFee, HeroImage, DigitalLibrary, ProductionUnit, DeanMessage
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage  # <-- ADD THIS
from django.http import JsonResponse


def home(request):
    # Get published news with pagination
    news_list = News.objects.filter(status='published').order_by('-published_date')
    paginator = Paginator(news_list, 3)  # Show 3 news items per page
    page_number = request.GET.get('page')
    news_items = paginator.get_page(page_number)

    # Get departments
    # Only active departments
    departments = Department.objects.filter(status='published')
    stats = Statistic.objects.filter(status='published')
    testimonials = Testimonial.objects.filter(status='published')
    hero_images = HeroImage.objects.all() 
    # Send both to template
    return render(request, 'home.html', {
        'news_items': news_items,
        'departments': departments,
        "stats": stats,
        "testimonials": testimonials,
        'hero_images': hero_images,  # <-- pass hero images to template
    })
def about (request):
    return render(request, 'about.html')
def missionandvision (request):
    return render(request, 'missionandvision.html')
def deanmessage (request):
    return render(request, 'missionandvision.html')
def events(request):
    return render(request, 'events.html')
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk, status="published")
    return render(request, "department.html", {"department": department})
def contact(request):
    form = ContactForm()  # instantiate an empty form
    return render(request, 'contact.html', {"form": form})
def news_list(request):
    news_items = News.objects.all().order_by('-published_date')
    paginator = Paginator(news_items, 6)  # 6 news per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})
def selectedNews(request, news_id):
    # fetch the clicked news item
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'newsdetail.html', {'news': news_item})

def vacancy_list(request):
    vacancies = Vacancy.objects.filter(status='published').order_by('-published_date')
    
    # Pagination: 6 vacancies per page
    paginator = Paginator(vacancies, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'vacancies.html', {'page_obj': page_obj})

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})
def tuitionfee_list(request):
    fees = TuitionFee.objects.all()
    return render(request, "tuitionfee_list.html", {"fees": fees})

def digital_library_list(request):
    digital_libraries = DigitalLibrary.objects.filter(status='published').order_by('-published_date')
    
    # Pagination: 6 digital libraries per page
    paginator = Paginator(digital_libraries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'digital_libraries.html', {'page_obj': page_obj})

def digital_library_detail(request, dig_id):
    digital_library = get_object_or_404(DigitalLibrary, id=dig_id)
    return render(request, 'digital_library_detail.html', {'digital_library': digital_library})

def production_unit_list(request):
    production_units = ProductionUnit.objects.filter(status='published').order_by('-published_date')
    
    # Pagination: 6 production units per page
    paginator = Paginator(production_units, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'production_units.html', {'page_obj': page_obj})

def production_unit_detail(request, unit_id):
    production_unit = get_object_or_404(ProductionUnit, id=unit_id)
    return render(request, 'production_unit_detail.html', {'production_unit': production_unit})

def tender_list(request):
    tenders = Tender.objects.filter(status='published').order_by('-published_date')
    
    # Pagination: 6 tenders per page
    paginator = Paginator(tenders, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tenders.html', {'page_obj': page_obj})

def tender_detail(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    return render(request, 'tender_detail.html', {'tender': tender})

def send_contact_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\n{message}"

            try:
                email_msg = EmailMessage(
                    subject=subject,
                    body=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],  # You will receive the email
                    reply_to=[email]                # Replies go to the user
                )
                email_msg.send(fail_silently=False)  # Try sending the email

                return JsonResponse({
                    'success': True,
                    'message': 'Your message has been sent successfully!'
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': f'Error sending message: {str(e)}'
                })
        else:
            # Form is invalid
            return JsonResponse({
                'success': False,
                'message': 'Form validation failed.',
                'errors': form.errors.as_json()
            })

    # Not a POST request
    return JsonResponse({'success': False, 'message': 'Invalid request'})