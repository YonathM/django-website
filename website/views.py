from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News, Department, Statistic, Testimonial, Vacancy
from django.core.mail import send_mail
from .forms import ContactForm

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
    # Send both to template
    return render(request, 'home.html', {
        'news_items': news_items,
        'departments': departments,
        "stats": stats,
        "testimonials": testimonials
    })
def about (request):
    return render(request, 'about.html')
def missionandvision (request):
    return render(request, 'missionandvision.html')
def events(request):
    return render(request, 'events.html')
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk, status="published")
    return render(request, "department.html", {"department": department})
def contact(request):
    return render(request, 'contact.html')
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

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    EMAIL_HOST_USER,  # sender
                    [EMAIL_HOST_USER],  # send to yourself
                    fail_silently=False
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Error sending message: {str(e)}")

            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})