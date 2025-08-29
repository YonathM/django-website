from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Department, Statistic, Testimonial, Vacancy

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
def events(request):
    return render(request, 'events.html')
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

